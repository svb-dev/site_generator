from textnode import TextNode, TextType
from split_images_and_links import split_nodes_image, split_nodes_link
import unittest


class TestHTMLNode(unittest.TestCase):

    def test_one_image_node(self):
        old_nodes = [TextNode(
            "This is text with an ![first image](https://i.imgur.com/zjjcJKZ.png) the end.",
            TextType.TEXT)]
        output_list = split_nodes_image(old_nodes)

        self.assertEqual(output_list, [TextNode("This is text with an ", TextType.TEXT), TextNode(
            "first image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" the end.", TextType.TEXT)])

    def test_two_image_nodes(self):

        old_nodes = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) END TEXT",
                              TextType.TEXT)]
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(output_list, [TextNode("This is text with an ", TextType.TEXT), TextNode(
            "image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and another ", TextType.TEXT), TextNode(
            "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"), TextNode(" END TEXT", TextType.TEXT)])

    def test_image_beginning(self):
        old_nodes = [TextNode(
            "![first image](https://i.imgur.com/zjjcJKZ.png) the end.)", TextType.TEXT)]
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(output_list, [TextNode(
            "first image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" the end.)", TextType.TEXT)])

    def test_image_end(self):
        old_nodes = [TextNode(
            "some leading text ![first image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)]
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(output_list, [TextNode("some leading text ", TextType.TEXT), TextNode(
            "first image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")])

    def test_only_image(self):
        old_nodes = [TextNode(
            "![first image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)]
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(output_list, [TextNode(
            "first image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")])

    def test_empty_list(self):
        old_nodes = []
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(output_list, [])

    def test_empty_textnode_string(self):
        old_nodes = [TextNode("", TextType.TEXT)]
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(output_list, [TextNode("", TextType.TEXT)])

    def test_non_text_type_node(self):
        old_nodes = [TextNode("**bold text**", TextType.BOLD)]
        output_list = split_nodes_image(old_nodes)
        self.assertEqual(
            output_list, [TextNode("**bold text**", TextType.BOLD)])

# TEST FOR LINKS

    def test_one_link_node(self):
        old_nodes = [TextNode(
            "This is text with a [first link](https://www.bbc.com/) the end.",
            TextType.TEXT)]
        output_list = split_nodes_link(old_nodes)

        self.assertEqual(output_list, [TextNode("This is text with a ", TextType.TEXT), TextNode(
            "first link", TextType.LINK, "https://www.bbc.com/"), TextNode(" the end.", TextType.TEXT)])

    def test_two_link_nodes(self):

        old_nodes = [TextNode("This is text with a [first link](https://www.bbc.com/) and another [second link](https://www.cbc.com) END TEXT",
                              TextType.TEXT)]
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(output_list, [TextNode("This is text with a ", TextType.TEXT), TextNode(
            "first link", TextType.LINK, "https://www.bbc.com/"), TextNode(" and another ", TextType.TEXT), TextNode(
            "second link", TextType.LINK, "https://www.cbc.com"), TextNode(" END TEXT", TextType.TEXT)])

    def test_link_beginning(self):
        old_nodes = [TextNode(
            "[first link](https://www.bbc.com/) the end.)", TextType.TEXT)]
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(output_list, [TextNode(
            "first link", TextType.LINK, "https://www.bbc.com/"), TextNode(" the end.)", TextType.TEXT)])

    def test_link_end(self):
        old_nodes = [TextNode(
            "some leading text [first link](https://www.bbc.com/)", TextType.TEXT)]
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(output_list, [TextNode("some leading text ", TextType.TEXT), TextNode(
            "first link", TextType.LINK, "https://www.bbc.com/")])

    def test_only_link(self):
        old_nodes = [TextNode(
            "[first link](https://www.bbc.com/)", TextType.TEXT)]
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(output_list, [TextNode(
            "first link", TextType.LINK, "https://www.bbc.com/")])

    def test_empty_link_list(self):
        old_nodes = []
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(output_list, [])

    def test_empty_textnode_string_link(self):
        old_nodes = [TextNode("", TextType.TEXT)]
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(output_list, [TextNode("", TextType.TEXT)])

    def test_non_text_type_node_link(self):
        old_nodes = [TextNode("**bold text**", TextType.BOLD)]
        output_list = split_nodes_link(old_nodes)
        self.assertEqual(
            output_list, [TextNode("**bold text**", TextType.BOLD)])


if __name__ == "__main__":
    unittest.main()
