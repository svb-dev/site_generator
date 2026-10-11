from parent_node import ParentNode
from leaf_node import LeafNode

child_node_1 = LeafNode("tag1", "val1", {"key1": "value1"})
child_node_2 = LeafNode("tag2", "val2")
child_node_3 = LeafNode("tag3", "val3")
parent_node_1 = ParentNode(
    "patg", [child_node_1, child_node_2, child_node_3])


parent_node_2 = ParentNode("div", [])

child1 = LeafNode("t1", "v1")
parent_node_3 = ParentNode("tag", [])


# nested parent node:

leaf_node = LeafNode("tag7", "val7", {"key7": "val7"})
parent_node_6 = ParentNode("tag6", [leaf_node])
parent_node_5 = ParentNode("tag5", [parent_node_6])
parent_node_4 = ParentNode("tag4", [parent_node_5])


print(parent_node_4.to_html())
