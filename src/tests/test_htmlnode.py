import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nodes import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_initialization(self):
        node = HTMLNode(
            "div",
            "Hello World",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(
            node.props, {"href": "https://www.google.com", "target": "_blank"}
        )

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(tag="img", props={"src": "logo.png"})
        self.assertEqual(node.props_to_html(), ' src="logo.png"')


if __name__ == "__main__":
    unittest.main()
