from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag : str, children : list[HTMLNode], props: dict[str,str] | None = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag name cannot be empty")
        if self.children is None:
            raise ValueError("Children cannot be None")

        return f"<{self.tag}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
