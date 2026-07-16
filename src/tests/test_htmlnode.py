import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nodes import (
    HTMLNode,
    LeafNode,
    ParentNode,
)


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_initialization(self):
        # Tests that the constructor sets attributes correctly
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
        # Test props_to_html with multiple properties
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
        # Test props_to_html when props is None (should return empty string)
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        # Test props_to_html with a single property
        node = HTMLNode(tag="img", props={"src": "logo.png"})
        self.assertEqual(node.props_to_html(), ' src="logo.png"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("p", "Hello, world!", {"class": "text"})
        self.assertEqual(node2.to_html(), '<p class="text">Hello, world!</p>')

        node3 = LeafNode("a", "Click here", {"href": "https://www.example.com"})
        self.assertEqual(
            node3.to_html(), '<a href="https://www.example.com">Click here</a>'
        )

    def test_leaf_to_html_empty_value(self):
        node = LeafNode("span", "")
        self.assertEqual(node.to_html(), "<span></span>")

    def test_leaf_to_html_no_props(self):
        node = LeafNode("div", "Content")
        self.assertEqual(node.to_html(), "<div>Content</div>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("button", "Click me", {"type": "button", "class": "btn"})
        self.assertEqual(
            node.to_html(), '<button type="button" class="btn">Click me</button>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "No tag")
        node2 = LeafNode("", "No tag")
        self.assertEqual(node.to_html(), "No tag")
        self.assertEqual(node2.to_html(), "No tag")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
