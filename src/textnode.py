class TextNode:
    def __init__(self, text, text_type, url):
        """
        Initialize the object with the provided text, text type, and URL.

        Parameters:
            text (str): The text to be stored in the object.
            text_type (str): The type of text being stored.
            url (str): The URL associated with the text.

        Returns:
            None
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Compares two TextNode objects for equality.

        Parameters:
        other (TextNode): The TextNode object to compare to.

        Returns:
        bool: True if all attributes of the two TextNode objects are equal,
              False otherwise.
        """
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
