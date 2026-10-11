class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag: str = tag
        self.value: str = value
        self.children: list = children
        self.props: dict = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or self.props == "":
            return ""
        result_string = "".join(
            f' {key}="{value}"' for key, value in self.props.items())

        return result_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
