import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # Returns an empty string if props is None.
    def test_props_to_html_none(self):
        """
        Test if props_to_html returns an empty string when props is None.
        """
        node = HTMLNode(tag="p", value="Hello World", props=None)
        result = node.props_to_html()
        assert result == ""

        # Returns the correct HTML attribute string for multiple key-value pairs in props.
    def test_correct_html_attribute_string(self):
        """
        Test if the props_to_html method returns the correct HTML attribute string for multiple key-value pairs in props.
        """
        # Create an HTMLNode object with multiple key-value pairs in props
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})

        # Call the props_to_html method
        result = node.props_to_html()

        # Check if the result is the correct HTML attribute string
        assert result == ' href="https://www.google.com" target="_blank"'
