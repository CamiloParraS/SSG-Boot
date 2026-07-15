from enum import Enum

class TextType(Enum):
    PLAIN = 1
    BOLD = 2
    ITALIC = 3
    CODE_TEXT = 4
    LINKS = 5
    IMAGES = 6

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None, image_url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"
