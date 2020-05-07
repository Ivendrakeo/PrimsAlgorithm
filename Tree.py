"""
Authors: Draven Schilling, Andy Iliescu
Date: 5/7/20
Course: CS 3851 - Algorithms (Final Project)
"""

import sys
from Graph import Vertex


class Tree:
    """
    Implements a basic multi-leaf tree structure.

    This implementation is NOT fully functional in that it is only meant
    to supplement a demonstration for Prim's Algorithm

    The implementation of this tree is not traditional. Tree nodes are stored
    in a python dictionary (Name: Node). This is in contrast to a linked-list
    style tree. The trade off is that it has a larger space complexity but
    is easier to implement and adding to the tree is O(1) which is important
    because we don't want it to impact the runtime of Prim's algorithm which
    builds a tree from a graph and expects an O(1) tree-inset time.
    """

    def __init__(self):
        self.test = 0
        self._parent = None
        this._nodes = dict()

    def add_node(self, parent, vertex):
        """

        :param parent: parent Vertex object
        :param vertex: new node Vertex object
        """
        pass

    def remove_node(self):
        # TODO (may not do)
        pass

    def print_tree(self):
        # TODO
        pass


class Node:

    """
    Tree helper class which stores individual node-related data.
    """

    def __init__(self, x, y, name, parent):
        # Cartesian x coordinate
        self._x = x
        # Cartesian y coordinate
        self._y = y
        # Node name. For Prim's should match graph node name
        self._name = name
        # parent Node object
        self._parent = parent
        # list of all siblings sharing the same parent node.
        self._siblings = set()

    def __str__(self):
        """
        TODO
        Simple to-string method which prints the object data members
        """
        pass

