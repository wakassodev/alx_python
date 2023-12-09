#!/usr/bin/python3
"""Contains the class BaseGeometry"""
class NoInitSubclassMeta(type):
    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']

class BaseGeometry(metaclass=NoInitSubclassMeta):
    """Empty class."""