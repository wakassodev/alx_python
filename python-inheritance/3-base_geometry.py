#!/usr/bin/python3
"""Contains the class BaseGeometry"""
class BaseGeometry:
    """Empty class."""

    def __dir__(self):
        """Exclude __init_subclass__ from the output of dir()."""
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
