class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes the HTMLNode with the provided tag, value, children, and props.
        tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        children - A list of HTMLNode objects representing the children of this node
        props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_hmtl(self):
        """
        Child classes will override this method to render themselves as HTML.
        """
        raise NotImplementedError("html method not implemented")

    def props_to_html(self):
        """
        A method that converts properties to HTML attributes and returns a string.
        """
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        """
        A special method used to return a printable representation of the object.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        """
        Initializes a LeafNode object.

        Args:
            tag (str, optional): The HTML tag for the node. Defaults to None.
            value (str, optional): The value/content of the node. Defaults to None.
            props (dict, optional): The properties/attributes of the node. Defaults to None.
        """
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        Converts the LeafNode object to its HTML representation.

        Returns:
            str: The HTML representation of the LeafNode object.

        Raises:
            ValueError: If the value of the node is None.
        """
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        """
        Returns a string representation of the LeafNode object.

        Returns:
            str: The string representation of the LeafNode object.
        """
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
