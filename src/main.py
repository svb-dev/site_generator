from textnode import TextNode, TextType
import os
import shutil
from generate_pages_recursive import generate_pages_recursive
from copy_static import copy_static
# print("hello world")


# def main():
#    obj = TextNode("test text", TextType.LINKS_FORMAT.value,
#                   "https://www.boot.dev")
#    print(f"TextNode({obj})")


# copy_static("static", "public")

generate_pages_recursive(
    "content", "template.html", "public")
