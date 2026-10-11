from extract_links import extract_markdown_images, extract_markdown_links
import unittest


class TestModule(unittest.TestCase):
    def test_link_many(self):
        markdown_input = "This is text with a link1 [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev). link3 [to bbc](https://www.bbc.com)"
        output = extract_markdown_links(markdown_input)
        self.assertEqual(output, [("to boot dev", "https://www.boot.dev"), ("to youtube",
                         "https://www.youtube.com/@bootdotdev"), ("to bbc", "https://www.bbc.com")])

    def test_plain_text_links(self):
        markdown_input = "This is text with a link1  and link . link3 not text"
        output = extract_markdown_links(markdown_input)
        self.assertEqual(output, [])

    def test_image_many(self):
        markdown_input = "This is text with a link1 ![doggy](www.doggy.com/file.jpg) and ![cat](www.pic.com/cat/jpg). link3 ![tree](www.tree.jpg)"
        output = extract_markdown_images(markdown_input)
        self.assertEqual(output, [("doggy", "www.doggy.com/file.jpg"),
                         ("cat", "www.pic.com/cat/jpg"), ("tree", "www.tree.jpg")])

    def test_extract_markdown_links_with_images(self):
        markdown_input = "This is text with a link1 ![doggy](www.doggy.com/file.jpg) and ![cat](www.pic.com/cat/jpg). link3 ![tree](www.tree.jpg)"
        output = extract_markdown_links(markdown_input)
        self.assertEqual(output, [])

    def test_extract_markdown_images_with_links(self):
        markdown_input = "This is text with a link1 [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev). link3 [to bbc](https://www.bbc.com)"
        output = extract_markdown_images(markdown_input)
        self.assertEqual(output, [])
