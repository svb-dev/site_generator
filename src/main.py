import os
import shutil
import sys

from generate_pages_recursive import generate_pages_recursive
from copy_static import copy_static

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


# OCT 12 - modify generate_page and generate_pages_recursive
# to accept basepath as the 4th argument

def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory ...")
    copy_static(dir_path_static, dir_path_public)

    print("Generating content...")

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    generate_pages_recursive(
        dir_path_content, template_path, dir_path_public, basepath)


main()
