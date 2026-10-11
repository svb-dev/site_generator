from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode
from parent_node import ParentNode
from leaf_node import LeafNode
from textnode import TextType, TextNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

# This is my code


def markdown_to_html_node(markdown):
    # markdown_to_blocks(markdown) returns a list of blocks
    accumulated_list = []
    blocks_list = markdown_to_blocks(markdown)
    for block in blocks_list:
        # print(repr(block))
        block = block.strip()
        block_type = block_to_block_type(block)
        # print(block_type)
        if block_type == BlockType.HEADING:
            # heading_count is a number 1- 6 . to get the tag
            # use f"h{heading_count}"
            heading_count = block.split(" ")[0].count("#")
            stripped_block = strip_markers("#", block)
            parent_node_h = ParentNode(
                f"h{heading_count}", text_to_children(stripped_block))
            accumulated_list.append(parent_node_h)
            # print(f"<h{heading_count}>{children}</h{heading_count}>")

        elif block_type == BlockType.PARAGRAPH:
            block_lst = block.split("\n")
            block = " ".join(block_lst)
            parent_node_b = ParentNode("p", text_to_children(block))
            accumulated_list.append(parent_node_b)

        elif block_type == BlockType.QUOTE:
            block_lst = block.split("\n")
            new_block_lst = []
            for line in block_lst:
                if line != "":
                    line = line.strip(">").lstrip()
                    if line != "":
                        new_block_lst.append(line)
            new_block = " ".join(new_block_lst)
            one_big_blockquote = ParentNode(
                "blockquote", text_to_children(new_block))
            # q_list.append(parent_quote_node)
            # parent_node_q_list = ParentNode("blockquote", q_list)
            # accumulated_list.append(parent_node_q_list)
            accumulated_list.append(one_big_blockquote)

        elif block_type == BlockType.CODE:
            stripped_block = block[4:-3]
            print(repr(stripped_block))
            code_text_node = TextNode(stripped_block, TextType.CODE)
            code_html_node = text_node_to_html_node(code_text_node)
            list_code_html_node = []
            list_code_html_node.append(code_html_node)
            parent_node_c = ParentNode(
                "pre", list_code_html_node)
            accumulated_list.append(parent_node_c)

        elif block_type == BlockType.UNORDERED_LIST:
            block_lst = block.split("\n")
            u_list = []
            for u_list_item in block_lst:
                u_list_item = u_list_item[2:]
                parent_node_u = ParentNode(
                    "li", text_to_children(u_list_item))
                u_list.append(parent_node_u)
            parent_node_u_list = ParentNode("ul", u_list)
            accumulated_list.append(parent_node_u_list)

        elif block_type == BlockType.ORDERED_LIST:
            block_lst = block.split("\n")
            o_list = []
            i = 1
            for o_list_item in block_lst:
                o_list_item = o_list_item.lstrip(f"{i}. ")
                parent_o_node = ParentNode("li", text_to_children(o_list_item))
                # o_list is  a list of Leaf Nodes with tag "li"
                o_list.append(parent_o_node)
                i += 1
            parent_node_o_list = ParentNode("ol", o_list)
            accumulated_list.append(parent_node_o_list)

        else:
            raise ValueError("unexpected block type")

    top_parent = ParentNode("div", accumulated_list)
    return (top_parent)
    # print(top_parent.to_html())
    # print(f"<div>{accumulated_list.to_html()}</div>")
    # return (html_node.to_html())


def text_to_children(text: str) -> list[TextNode]:
    text_nodes_list = text_to_textnodes(text)
    leaf_node_list = []
    for text_node in text_nodes_list:
        leaf_node_list.append(text_node_to_html_node(text_node))
    return leaf_node_list


# strips markers and space after it
def strip_markers(marker: str, text: str) -> str:
    depth = 0
    for char in text:
        if char == marker:
            depth += 1
        else:
            break
    return text[depth:].lstrip()


md_para = """
this is a paragraph with **bold text**
this is the second paragraph with an image ![Description of image](url/of/image.jpg)
**bold text**
"""

md_u_list = """
- this is an unordered list
- this is second item with a list with a **bold text**
- _italic words_
"""

md_o_list = """
1. First item
2. Second item with a **bold text**
3. Third item
"""

md_heading = """
# this is a heading with _italics_ and **bold**
"""

md_quote = """
> this is a blockquote with **bold text**
> this is the second quote with an ![image](https://www.pix.com/231.jpg)
"""

md_code = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""


output = markdown_to_html_node(md_code)

print(output.to_html())
# (self, tag=None, value=None, children=None, props=None):
