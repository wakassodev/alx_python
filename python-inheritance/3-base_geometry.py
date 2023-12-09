#!/usr/bin/python3
"""Contains the class BaseGeometry"""
class BaseGeometry:
    """Empty class."""

    def __dir__(self):
        if hasattr(self, '__dict__'):
            # For instances, exclude __init_subclass__ from the dir
            return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
        else:
            # For the class itself, include __init_subclass__ in dir
            return dir(type(self))