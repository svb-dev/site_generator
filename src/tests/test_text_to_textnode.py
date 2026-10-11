from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
import unittest


class TestInLineMarkdown(unittest.TestCase):

    def test_different_type_node(self):
        old_nodes = "This is **bold text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output_list = text_to_textnodes(old_nodes)
        self.assertEqual(output_list, [TextNode("This is ", TextType.TEXT), TextNode("bold text", TextType.BOLD),
                                       TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(
                                           " word and a ", TextType.TEXT), TextNode("code block", TextType.CODE),
                                       TextNode(" and an ", TextType.TEXT), TextNode(
                                           "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT),
                                       TextNode("link", TextType.LINK, "https://boot.dev")])

    def test_plain_text(self):
        old_text = "plain text no markdown"
        output = text_to_textnodes(old_text)
        self.assertEqual(output, [TextNode(
            "plain text no markdown", TextType.TEXT)])

    def test_only_link(self):
        old_text = "This is a text with a [link](https://boot.dev)"
        output = text_to_textnodes(old_text)
        self.assertEqual(output, [TextNode("This is a text with a ", TextType.TEXT), TextNode(
            "link", TextType.LINK, "https://boot.dev")])

    def test_two_images(self):
        old_text = "Image one is ![image1](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjLj7aCOwNpKr7N6o52F1ZWPxNrJVQX9T8HgmKCvmKjA&s=10) and image two is ![cat](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoMQVa--RBfnEtDtTFqFyTJip-sf6S6CL1JAOw39ZeRw&s=10)"
        output = text_to_textnodes(old_text)
        self.assertEqual(output, [TextNode("Image one is ", TextType.TEXT), TextNode(
            "image1", TextType.IMAGE, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjLj7aCOwNpKr7N6o52F1ZWPxNrJVQX9T8HgmKCvmKjA&s=10"), TextNode(" and image two is ", TextType.TEXT), TextNode("cat", TextType.IMAGE, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoMQVa--RBfnEtDtTFqFyTJip-sf6S6CL1JAOw39ZeRw&s=10")])

    def test_ends_delimiter(self):
        old_text = "Old text sentence **bold text**"
        output = text_to_textnodes(old_text)
        self.assertEqual(output, [TextNode("Old text sentence ",
                         TextType.TEXT), TextNode("bold text", TextType.BOLD)])


if __name__ == "__main__":
    unittest.main()
