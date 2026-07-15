import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test equality of two TextNode instances with the same text and type
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        # Test inequality of two TextNode instances with different text
        node3 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node3)

        # Test inequality of two TextNode instances with different types
        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node4)

        # Test when the url attribute is set to None
        node5 = TextNode("This is a text node", TextType.LINKS, url=None)
        node6 = TextNode("This is a text node", TextType.LINKS)
        self.assertEqual(node5, node6)

        # Test when the url attribute is set to a value
        node7 = TextNode("This is a text node", TextType.LINKS, url="https://example.com")
        node8 = TextNode("This is a text node", TextType.LINKS, url="https://example.com")
        self.assertEqual(node7, node8)

        # Test inequality of two TextNode instances with different url values
        node9 = TextNode("This is a text node", TextType.LINKS, url="https://example.com")
        node10 = TextNode("This is a text node", TextType.LINKS, url="https://different.com")
        self.assertNotEqual(node9, node10)

        # Test inequality between urls and images
        node11 = TextNode("This is a text node", TextType.LINKS, url="https://example.com")
        node12 = TextNode("This is a text node", TextType.IMAGES, url="https://example.com")
        self.assertNotEqual(node11, node12)

if __name__ == "__main__":
    unittest.main()
