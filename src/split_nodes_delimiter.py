from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(
                    TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

# INPUT node with an empty string :
# text_node_list = [TextNode("", TextType.TEXT)]
# print(split_nodes_delimiter(text_node_list, "**", TextType.BOLD))
# ---------------
# text_node_list = [
#   TextNode("This is text with a **bolded _italic phrase_ phrase** in the middle", TextType.TEXT)]

# x = split_nodes_delimiter(text_node_list, "**", TextType.BOLD)
# y = split_nodes_delimiter(text_node_list, "_", TextType.ITALIC)
# print(y)

# lst = []

# lst.append(TextNode("texdfsrte", TextType.TEXT))

#   print(lst)

# input_list = [TextNode("Text node one _bold text_ end of sentence", TextType.TEXT), TextNode(
#    "Text node two `code text` end of sentence", TextType.TEXT)]

# output_list = split_nodes_delimiter(input_list, "_", TextType.BOLD)

# print(output_list)
