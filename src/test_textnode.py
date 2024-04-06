import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """
        Test if the TextNode objects created are equal using the assertEqual method.
        """
        node = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://example.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        """
        Test if the string representation of the TextNode object is correct.
        """
        node = TextNode("This is a text node", "bold", "http://example.com")
        self.assertEqual(str(node), "TextNode(This is a text node, bold, http://example.com)")

    def test_url(self):
        """
        Tests if URL is set correctly.
        """
        node = TextNode("This is a text node", "bold", "http://example.com")
        # Check if either URL is None and return False if so
        self.assertEqual(node.url, "http://example.com")

    def test_text_node_equality(self):
        """
        Test nodes with different content or style are not equal
        """
        # Test nodes with different content or style are not equal
        node1 = TextNode("Content A", "style1", "http://example.com")
        node2 = TextNode("Content A", "style2", "http://example.com")
        node3 = TextNode("Content B", "style1", "http://example.com")
        node4 = TextNode("Content B", "style2", "http://example.com")

        self.assertNotEqual(node1, node2, "Nodes with different styles should not be equal")
        self.assertNotEqual(node1, node3, "Nodes with different contents should not be equal")
        self.assertNotEqual(node1, node4, "Nodes with different contents and styles should not be equal")
        self.assertNotEqual(node2, node3, "Nodes with different contents and styles should not be equal")

        # Test nodes with the same content and style are equal
        node5 = TextNode("Content A", "style1", "http://example.com")
        self.assertEqual(node1, node5, "Nodes with the same content and style should be equal")


if __name__ == '__main__':
    unittest.main()
