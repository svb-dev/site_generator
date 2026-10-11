from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
import unittest


class TestModule(unittest.TestCase):
    def test_snd_code(self):
        input_list = [TextNode(
            "This is a sentence with a `code phrase` in the middle.", TextType.TEXT)]
        output_list = split_nodes_delimiter(input_list, "`", TextType.CODE)

        self.assertEqual(output_list, [TextNode("This is a sentence with a ", TextType.TEXT), TextNode(
            "code phrase", TextType.CODE), TextNode(" in the middle.", TextType.TEXT)])

    def test_snd_bold_start(self):
        input_list = [
            TextNode("_bold text_ this is a sentence with bold text", TextType.TEXT)]
        output_list = split_nodes_delimiter(input_list, "_", TextType.BOLD)

        self.assertEqual(output_list, [TextNode("bold text", TextType.BOLD), TextNode(
            " this is a sentence with bold text", TextType.TEXT)])

    def test_snd_non_text(self):
        input_list = [
            TextNode("this is not a text type node.", TextType.ITALIC)]
        output_list = split_nodes_delimiter(input_list, "`", TextType.CODE)

        self.assertEqual(output_list, [TextNode(
            "this is not a text type node.", TextType.ITALIC)])

    def test_snd_many_nodes(self):
        input_list = [TextNode("Text node one _bold text_ end of sentence", TextType.TEXT), TextNode(
            "Text node two _bold text_ end of sentence", TextType.TEXT)]
        output_list = split_nodes_delimiter(input_list, "_", TextType.BOLD)
        self.assertEqual(output_list, [TextNode("Text node one ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(
            " end of sentence", TextType.TEXT), TextNode("Text node two ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" end of sentence", TextType.TEXT)])


if __name__ == "__main__":
    unittest.main()
