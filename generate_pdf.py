import os
import re
import glob
import subprocess

def convert_links_to_footnotes(content, footnote_start=1):
    footnotes = []
    footnote_counter = footnote_start
    
    def looks_like_url(text, link):
        """Check if the link text itself looks like a URL."""
        return (
            text == link or
            re.fullmatch(r'https?://\S+', text) or     # full URL
            re.fullmatch(r'\S+\.\S+(/\S*)?', text)     # domain or domain/path
        )
    
    def replacer(match):
        nonlocal footnote_counter
        text = match.group(1)
        link = match.group(2)
        
        # Skip conversion if text looks like a URL
        if looks_like_url(text, link):
            return match.group(0)
        
        # Create footnote for every link
        footnotes.append(link)
        current_footnote = footnote_counter
        footnote_counter += 1
        return f"{text}[^{current_footnote}]"
    
    # Process all links in the content
    processed_content = re.sub(r'\[([^\]]+?)\]\((https?://[^\s)]+)\)', replacer, content)
    
    # Add footnotes section if any footnotes were created
    if footnotes:
        footnotes_section = "\n\n"
        for i, url in enumerate(footnotes, footnote_start):
            footnotes_section += f"[^{i}]: {url}\n"
        processed_content += footnotes_section
    
    return processed_content, footnote_counter

def convert_links(content):
    """Convert [text](url) to [text (url)](url), unless text looks like a URL."""
    def looks_like_url(text):
        return (
            text == link or
            re.fullmatch(r'https?://\S+', text) or     # full URL
            re.fullmatch(r'\S+\.\S+(/\S*)?', text)     # domain or domain/path
        )

    def replacer(match):
        text = match.group(1)
        global link
        link = match.group(2)

        if looks_like_url(text):
            return match.group(0)

        if text.endswith(f' ({link})'):
            return match.group(0)

        return f'[{text} ({link})]({link})'

    return re.sub(r'\[([^\]]+?)\]\((https?://[^\s)]+)\)', replacer, content)

def convert_and_save_markdown(source_dir, dest_dir):
    """Convert and save markdown files to a new directory."""
    global_footnote_counter = 1  # Track footnotes across all files
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, source_dir)

                # Skip if we're already in the printed subdirectory
                if rel_path.startswith("printed" + os.sep):
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
print_dir = "./source/print"
output_original_pdf = "maintainers.pdf"
output_print_pdf = "maintainers_print.pdf"

# --- Execution ---
convert_and_save_markdown(source_dir, print_dir)
run_pandoc(source_dir, output_original_pdf)
run_pandoc(print_dir, output_print_pdf)
