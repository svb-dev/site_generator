from parent_node import ParentNode
from leaf_node import LeafNode
import unittest


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span><b>grandchild</b></span></div>")

    def test_to_html_many_children(self):
        child_node_1 = LeafNode("tag1", "val1", {"key1": "value1"})
        child_node_2 = LeafNode("tag2", "val2")
        child_node_3 = LeafNode("tag3", "val3")
        parent_node = ParentNode(
            "patg", [child_node_1, child_node_2, child_node_3])

        self.assertEqual(parent_node.to_html(
        ), '<patg><tag1 key1="value1">val1</tag1><tag2>val2</tag2><tag3>val3</tag3></patg>')

    def test_to_html_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_no_tag(self):
        child1 = LeafNode("t1", "v1")
        parent_node = ParentNode(None, [child1])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_nested_parents(self):
        leaf_node = LeafNode("tag7", "val7", {"key7": "val7"})
        parent_node_6 = ParentNode("tag6", [leaf_node])
        parent_node_5 = ParentNode("tag5", [parent_node_6])
        parent_node_4 = ParentNode("tag4", [parent_node_5])

        self.assertEqual(parent_node_4.to_html(
        ), '<tag4><tag5><tag6><tag7 key7="val7">val7</tag7></tag6></tag5></tag4>')


if __name__ == "__main__":
    unittest.main()
