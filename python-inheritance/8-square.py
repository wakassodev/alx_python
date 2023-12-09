#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        super().__init__(size, size)