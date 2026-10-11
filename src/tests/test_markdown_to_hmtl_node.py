from markdown_to_html_node import markdown_to_html_node
import unittest


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        md = """
This is a

# heading

## second heading

the end.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a</p><h1>heading</h1><h2>second heading</h2><p>the end.</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        # node = markdown_to_html_node(md)
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):

        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        # node = markdown_to_html_node(md)

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):

        md = """
- First item with a **bold text**
- Second item
- Third item
- Fourth item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><ul><li>First item with a <b>bold text</b></li><li>Second item</li><li>Third item</li><li>Fourth item</li></ul></div>")

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
4. Fourth item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><ol><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item</li></ol></div>")

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> this is a blockquote with **bold text**
> this is the second quote with an ![image](https://www.pix.com/231.jpg)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, '<div><blockquote>this is a blockquote with <b>bold text</b> this is the second quote with an <img src="https://www.pix.com/231.jpg" alt="image"></blockquote></div>')


if __name__ == "__main__":
    unittest.main()
