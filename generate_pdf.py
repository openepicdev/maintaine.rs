import os
import re
import glob
import subprocess

def find_existing_footnotes(content):
    """Find all existing footnote numbers in the content."""
    existing_footnotes = set()
    
    # Find footnote references like [^1], [^2], etc.
    footnote_refs = re.findall(r'\[\^(\d+)\]', content)
    for ref in footnote_refs:
        existing_footnotes.add(int(ref))
    
    # Find footnote definitions like [^1]: url
    footnote_defs = re.findall(r'^\[\^(\d+)\]:', content, re.MULTILINE)
    for def_num in footnote_defs:
        existing_footnotes.add(int(def_num))
    
    return existing_footnotes

def extract_reference_links(content):
    """Extract reference-style link definitions and return cleaned content."""
    reference_links = {}
    
    # Pattern for reference link definitions: [label]: url "optional title"
    ref_pattern = r'^\s*\[([^\]]+)\]:\s*(\S+)(?:\s+"([^"]*)")?\s*$'
    
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        match = re.match(ref_pattern, line)
        if match:
            label = match.group(1).lower()  # Reference labels are case-insensitive
            url = match.group(2)
            title = match.group(3) if match.group(3) else None
            reference_links[label] = {'url': url, 'title': title}
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines), reference_links

def convert_links_to_footnotes(content, footnote_start=1):
    """Convert inline and reference links to footnotes, respecting existing footnotes."""
    footnotes = []
    
    # Find existing footnotes to avoid conflicts
    existing_footnotes = find_existing_footnotes(content)
    
    # Start from the next available footnote number
    footnote_counter = footnote_start
    while footnote_counter in existing_footnotes:
        footnote_counter += 1
    
    # Extract reference links and clean content
    cleaned_content, reference_links = extract_reference_links(content)
    
    def looks_like_url(text, link):
        """Check if the link text itself looks like a URL."""
        return (
            text == link or
            re.fullmatch(r'https?://\S+', text) or     # full URL
            re.fullmatch(r'\S+\.\S+(/\S*)?', text)     # domain or domain/path
        )
    
    def inline_link_replacer(match):
        nonlocal footnote_counter
        text = match.group(1)
        link = match.group(2)
        
        # Skip conversion if text looks like a URL
        if looks_like_url(text, link):
            return match.group(0)
        
        # Create footnote for the link
        footnotes.append(link)
        current_footnote = footnote_counter
        footnote_counter += 1
        
        # Skip to next available footnote number
        while footnote_counter in existing_footnotes:
            footnote_counter += 1
            
        return f"{text}[^{current_footnote}]"
    
    def reference_link_replacer(match):
        nonlocal footnote_counter
        text = match.group(1)
        ref_label = match.group(2).lower() if match.group(2) else text.lower()
        
        # Look up the reference
        if ref_label in reference_links:
            link = reference_links[ref_label]['url']
            
            # Skip conversion if text looks like a URL
            if looks_like_url(text, link):
                return f"[{text}]({link})"
            
            # Create footnote for the reference link
            footnotes.append(link)
            current_footnote = footnote_counter
            footnote_counter += 1
            
            # Skip to next available footnote number
            while footnote_counter in existing_footnotes:
                footnote_counter += 1
                
            return f"{text}[^{current_footnote}]"
        else:
            # Reference not found, leave as is (will be broken link)
            return match.group(0)
    
    # Process inline links: [text](url)
    processed_content = re.sub(r'\[([^\]]+?)\]\((https?://[^\s)]+)\)', inline_link_replacer, cleaned_content)
    
    # Process reference links: [text][ref] or [text][] (where ref defaults to text)
    processed_content = re.sub(r'\[([^\]]+?)\]\[([^\]]*)\]', reference_link_replacer, processed_content)
    
    # Add footnotes section if any footnotes were created
    if footnotes:
        # Check if there's already a footnotes section
        if not re.search(r'^\[\^\d+\]:', processed_content, re.MULTILINE):
            processed_content += "\n\n"
        else:
            processed_content += "\n"
            
        # Add new footnotes using the actual footnote numbers assigned
        footnote_num = footnote_start
        while footnote_num in existing_footnotes:
            footnote_num += 1
            
        for url in footnotes:
            processed_content += f"[^{footnote_num}]: {url}\n"
            footnote_num += 1
            while footnote_num in existing_footnotes:
                footnote_num += 1
    
    return processed_content, footnote_counter



def convert_and_save_markdown(source_dir, dest_dir):
    """Convert and save markdown files to a new directory."""
    global_footnote_counter = 1  # Track footnotes across all files
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, source_dir)

                # Skip if we're already in the print subdirectory
                if rel_path.startswith("print" + os.sep):
                    continue

                dest_path = os.path.join(dest_dir, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                final_content, global_footnote_counter = convert_links_to_footnotes(
                    content, global_footnote_counter
                )

                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)

def run_pandoc(md_dir, output_pdf):
    """Run Pandoc to generate PDF from markdown files in a directory."""
    markdown_files = sorted(glob.glob(os.path.join(md_dir, "*.md")))

    if not markdown_files:
        print(f"No Markdown files found in {md_dir}")
        return

    pandoc_command = [
        "pandoc",
        *markdown_files,
        "--pdf-engine=pdflatex",
        "--from=markdown+raw_tex",
        "--template=eisvogel",
        "--metadata-file=./metadata.yaml",
        "--listings",
        "-o", output_pdf
    ]

    print(f"\nGenerating PDF: {output_pdf}")
    result = subprocess.run(pandoc_command)

    if result.returncode == 0:
        print(f"PDF created: {output_pdf}")
    else:
        print(f"Pandoc failed with exit code {result.returncode} for {output_pdf}")

# --- Configuration ---
source_dir = "./source"
print_dir = "./print"
output_original_pdf = "maintainers.pdf"
output_print_pdf = "maintainers_print.pdf"

# --- Execution ---
convert_and_save_markdown(source_dir, print_dir)
run_pandoc(source_dir, output_original_pdf)
run_pandoc(print_dir, output_print_pdf)