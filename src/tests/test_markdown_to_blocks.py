from markdown_to_blocks import markdown_to_blocks
import unittest


class TestMarkdownToBlocks(unittest.TestCase):

    def test_three_paragraphs(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,            [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ])

    def test_trailing_sentence(self):
        md = "  Sentence one   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Sentence one"])

    def test_with_link(self):
        md = """
This is a sentence with an image and a link

![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a sentence with an image and a link",
                                  "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"])

    def test_with_excessive_newlines(self):
        md = """

This is an example with empty blocks due to excessive newlines.



![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is an example with empty blocks due to excessive newlines.",
                                  "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"])

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()
