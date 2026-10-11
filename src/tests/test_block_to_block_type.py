from block_to_block_type import block_to_block_type, BlockType
import unittest


class TestBlockToBlockType(unittest.TestCase):

    def test_two_many_hashes_heading(self):
        old_block = "########### Heading 3 (Subsection)"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_two_heading(self):
        old_block = "## Heading 2 (Subsection)"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.HEADING)

    def test_paragraph(self):
        old_block = "JUst paragraph"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_code(self):
        old_block = "```\npython\ndef hello_world():\nprint('Hello, world!')```"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.CODE)

    def test_quote(self):
        old_block = "> this is a quote block"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.QUOTE)

    def test_unordered_list(self):
        old_block = "- this is an ordered list block - item two"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        old_block = "1. this is an ordered list block\n2. item two"
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.ORDERED_LIST)

    def test_multiline_code(self):
        old_block = """```
def hello():
    pass
```"""
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.CODE)

    def test_oneline_code(self):
        old_block = """```
        def hello():```"""
        output = block_to_block_type(old_block)
        self.assertEqual(output, BlockType.CODE)


if __name__ == "__main__":
    unittest.main()
