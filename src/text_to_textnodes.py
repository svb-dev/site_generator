from split_images_and_links import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def text_to_textnodes(text):

    text_node = [TextNode(text, TextType.TEXT)]
    t1 = split_nodes_delimiter(text_node, "`", TextType.CODE)
    t2 = split_nodes_delimiter(t1, "**", TextType.BOLD)
    t3 = split_nodes_delimiter(t2, "_", TextType.ITALIC)
    t4 = split_nodes_image(t3)
    t5 = split_nodes_link(t4)
    return t5


# text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

# print(text_to_textnodes(text))
