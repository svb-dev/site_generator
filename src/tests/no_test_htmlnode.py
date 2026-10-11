import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a HTML node", "test value")
        node2 = HTMLNode("This is a HTML node", "test value")
        repr_node = node.__repr__()
        repr_node2 = node2.__repr__()
        self.assertEqual(repr_node, repr_node2)

    def test_eq2(self):
        repr_node = HTMLNode(None, "test value", [
                             "child1", "child2"]).__repr__()
        repr_node2 = HTMLNode(None, "test value", [
                              "child1", "child2"]).__repr__()

        self.assertEqual(repr_node, repr_node2)

    def test_not_equal(self):
        repr_node = HTMLNode(children=["child1", "child2"], props={
                             "key1": "val1"}).__repr__()
        repr_node2 = HTMLNode(children=["child1", "child2"], props={
                              "k2": "v2"}).__repr__()
        self.assertNotEqual(repr_node, repr_node2)


if __name__ == "__main__":
    unittest.main()
