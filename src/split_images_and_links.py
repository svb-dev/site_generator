import re
from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError(
                    "invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(
                    TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(
                    TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


# old_nodes = [TextNode("This is text with a [first link](https://www.bbc.com/) END TEXT",
 #   TextType.TEXT)]
    # output_list = split_nodes_link(old_nodes)

    # for output in output_list:
    #    print(output)

    # 2nd VERSION :
    """
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    text_list = []
    new_nodes_list = []
    if len(old_nodes) == 0:
        return []

    for text_node in old_nodes:
        if text_node.text_type == TextType.TEXT:
            text = text_node.text
            pattern = r"(!\[[^\[\]]*\])(\([^\(\)]*\))"
            output_list = re.split(pattern, text)
            for output in output_list:
                if len(output) == 0:
                    continue
                else:
                    if bool(extract_markdown_images(output)):
                        new_image_node = TextNode(extract_markdown_images(
                            output)[0], TextType.IMAGE, extract_markdown_images(output)[1])
                        new_nodes_list.append(new_image_node)
                    else:
                        new_nodes_list.append(TextNode(output, TextType.TEXT))
        # Non Text nodes to be appended as is without any changes
        else:
            new_nodes_list.append(text_node)
    return new_nodes_list"""

    # FIRST VERSION :

    """def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

text_list = []
new_nodes_list = []
if len(old_nodes) == 0:
    return []

for text_node in old_nodes:
    if text_node.text_type != TextType.TEXT:
        new_nodes_list.append(text_node)
    else:
        text_list.append(text_node.text)

pattern = r"(!\[[^\[\]]*\])(\([^\(\)]*\))"

for text in text_list:
    output = re.split(pattern, text)
    if len(output) == 0:
        return TextNode("", TextType.TEXT)

    i = 0
    alt_text_pattern = r"(!\[[^\[\]]*\])"
    image_link_pattern = r"(\([^\(\)]*\))"
    while i < len(output):
        if bool(re.search(alt_text_pattern, output[i])) and bool(re.search(image_link_pattern, output[i+1])):
            new_node = TextNode(re.findall(
                r"!\[([^\[\]]*)\]", output[i])[0], TextType.IMAGE, re.findall(r"\(([^\(\)]*)\)", output[i+1])[0])
            new_nodes_list.append(new_node)
            i += 2
            continue
        elif len(output[i]) == 0:
            i += 1
            continue
        else:
            new_node = TextNode(output[i], TextType.TEXT)
            new_nodes_list.append(new_node)
        i += 1
return new_nodes_list"""
