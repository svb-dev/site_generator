from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import HTMLNode
import os


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_fhand = open(from_path)
    markdown_file = md_fhand.read()
    md_fhand.close()

    template_fhand = open(template_path)
    template_file = template_fhand.read()
    template_fhand.close()

    html_string = markdown_to_html_node(markdown_file).to_html()

    title = extract_title(markdown_file)

    new_hmtl = template_file.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_string)

    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_hmtl)
