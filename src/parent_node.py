from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    # tag: str, children: list[LeafNode]
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("the node has no tag")
        elif self.children is None:
            raise ValueError("the node has no children")
        else:
            inner_html = ""
            for child in self.children:
                inner_html += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
