import os
import re
import glob
import subprocess

def collect_all_existing_footnotes(source_dir):
    """First pass: collect all existing footnote numbers from all files."""
    all_existing_footnotes = set()
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, source_dir)
                
                # Skip if we're already in the print subdirectory
                if rel_path.startswith("print" + os.sep):
                    continue
                
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find footnote references and definitions
                footnote_refs = re.findall(r'\[\^(\d+)\]', content)
                for ref in footnote_refs:
                    all_existing_footnotes.add(int(ref))
    
    return all_existing_footnotes

def extract_reference_links(content):
    """Extract reference-style link definitions and return cleaned content."""
    reference_links = {}
    lines = content.split('\n')
    cleaned_lines = []
    
    # Pattern for reference link definitions: [label]: url "optional title"
    ref_pattern = r'^\s*\[([^\]]+)\]:\s*(\S+)(?:\s+"([^"]*)")?\s*$'
    
    for line in lines:
        match = re.match(ref_pattern, line)
        if match:
            label = match.group(1).lower()  # Reference labels are case-insensitive
            url = match.group(2)
            reference_links[label] = url
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines), reference_links

def looks_like_url(text, link):
    """Check if the link text itself looks like a URL."""
    return (
        text == link or
        re.fullmatch(r'https?://\S+', text) or     # full URL
        re.fullmatch(r'\S+\.\S+(/\S*)?', text)     # domain or domain/path
    )

def convert_file_links_to_footnotes(content, next_available_footnote, all_existing_footnotes):
    """Convert all links in a single file to footnotes."""
    # Extract reference links first
    cleaned_content, reference_links = extract_reference_links(content)
    
    # Collect all links to convert
    links_to_convert = []
    
    # Single comprehensive pattern to find all link types
    # This pattern matches:
    # 1. Inline links: [text](url)
    # 2. Reference links: [text][ref]
    # 3. Implicit reference: [text][]
    # 4. Shorthand reference: [text] (not followed by brackets, parens, or colon)
    link_pattern = r'\[([^\]^]+?)\](?:\[([^\]]*)\]|\((https?://[^\s)]+)\)|(?!\[|\(|:))'
    
    for match in re.finditer(link_pattern, cleaned_content):
        text = match.group(1)
        ref_label = match.group(2) if match.group(2) is not None else None
        inline_url = match.group(3)
        
        if inline_url:
            # Inline link [text](url)
            if not looks_like_url(text, inline_url):
                links_to_convert.append((match.span(), text, inline_url))
        else:
            # Reference-style link (explicit, implicit, or shorthand)
            if ref_label is not None:
                # Explicit [text][ref] or implicit [text][]
                lookup_label = ref_label.lower() if ref_label else text.lower()
            else:
                # Shorthand [ref]
                lookup_label = text.lower()
            
            if lookup_label in reference_links:
                url = reference_links[lookup_label]
                if not looks_like_url(text, url):
                    links_to_convert.append((match.span(), text, url))
    
    # Sort by position (reverse order to avoid position shifts when replacing)
    links_to_convert.sort(key=lambda x: x[0][0], reverse=True)
    
    # Assign footnote numbers and replace links
    footnote_counter = next_available_footnote
    url_to_footnote = {}  # Reuse footnote numbers for duplicate URLs
    footnote_definitions = []
    
    for (start, end), text, url in links_to_convert:
        if url not in url_to_footnote:
            # Find next available footnote number
            while footnote_counter in all_existing_footnotes:
                footnote_counter += 1
            
            url_to_footnote[url] = footnote_counter
            footnote_definitions.append(f"[^{footnote_counter}]: {url}")
            all_existing_footnotes.add(footnote_counter)  # Mark as used
            footnote_counter += 1
        
        # Replace the link with footnote reference
        footnote_num = url_to_footnote[url]
        replacement = f"{text}[^{footnote_num}]"
        cleaned_content = cleaned_content[:start] + replacement + cleaned_content[end:]
    
    # Add footnote definitions at the end
    if footnote_definitions:
        # Check if there are already footnote definitions
        if re.search(r'^\[\^\d+\]:', cleaned_content, re.MULTILINE):
            cleaned_content += "\n" + "\n".join(footnote_definitions) + "\n"
        else:
            cleaned_content += "\n\n" + "\n".join(footnote_definitions) + "\n"
    
    return cleaned_content, footnote_counter

def convert_and_save_markdown(source_dir, dest_dir):
    """Convert and save markdown files to a new directory."""
    # First pass: collect all existing footnotes across all files
    all_existing_footnotes = collect_all_existing_footnotes(source_dir)
    
    # Start numbering new footnotes after the highest existing one
    next_footnote = max(all_existing_footnotes) + 1 if all_existing_footnotes else 1
    
    # Second pass: process each file
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

                converted_content, next_footnote = convert_file_links_to_footnotes(
                    content, next_footnote, all_existing_footnotes
                )

                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(converted_content)

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