import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nodes import LeafNode


class TestLeafNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
