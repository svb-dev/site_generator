from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import HTMLNode
import os
import shutil
from pathlib import Path


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):

    print(
        f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")

    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
        os.mkdir(dest_dir_path)

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    template_fhand = open(template_path)
    template_file = template_fhand.read()
    template_fhand.close()

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f"Generating html from {from_path} to {dest_path}")

        if os.path.isfile(from_path):
            file_dest_path = Path(os.path.join(dest_dir_path, filename))

            md_fhand = open(from_path)
            markdown_file = md_fhand.read()
            md_fhand.close()

            html_string = markdown_to_html_node(markdown_file).to_html()
            title = extract_title(markdown_file)

            new_hmtl = template_file.replace(
                "{{ Title }}", title).replace("{{ Content }}", html_string)

            html_suffix_path = file_dest_path.with_suffix(".html")

            with open(html_suffix_path, "w") as f:
                f.write(new_hmtl)

        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    # dir_name = os.path.dirname(dest_path)
    # os.makedirs(dir_name, exist_ok=True)
    # with open(dest_path, "w") as f:
    #    f.write(new_hmtl)
