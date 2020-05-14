"""
Authors: Draven Schilling, Andy Iliescu
Date: 5/7/20
Course: CS 3851 - Algorithms (Final Project)
"""

import sys
from Graph import Vertex


class Tree:
    """
    Implements a basic multi-leaf tree-like structure.

    This implementation is NOT fully functional in that it is only meant
    to supplement a demonstration for Prim's Algorithm

    The implementation of this tree is not traditional because traversal methods
    are not needed for this application. Tree nodes are stored
    in a python dictionary (Name: Node). This is in contrast to a linked-list
    style tree. The trade off is that it has a larger space complexity but
    is easier to implement and adding to the tree is O(1) which is important
    because we don't want it to impact the runtime of Prim's algorithm which
    builds a tree from a graph and expects an O(1) tree-inset time.
    """

    def __init__(self):
        self._parent = None
        # Key = node.name , Value = Node obj
        self._nodes = dict()

    def add_node(self, parent, vertex):
        """
        Adds the vertex to the tree under the parent-associated node.
        :param parent: parent Vertex object
        :param vertex: new node Vertex object
        """
        node = Node(vertex.x, vertex.y, vertex.name, parent=None)
        if self._parent is None:
            self._parent = node
        else:
            nodes = self._nodes.keys()
            if parent.name in nodes and vertex.name not in nodes:
                node.parent = self._nodes[parent.name]
                self._nodes[parent.name].children.add(node)
            else:
                return False
        self._nodes[node.name] = node
        return True

    def remove_node(self):
        # TODO (may not do)
        pass

    def get_connections(self):
        """
        Get's a list of all connected nodes from the tree
        (source node, destination node).
        Useful for Prims output
        :return: list of all connected nodes
        """
        out = []
        nodes = self._nodes.values()
        for node in nodes:
            for child in node.children:
                out.append((node, child))
        return out

    def print_tree(self):
        """
        Print's the tree to the console in a (somewhat)
        readable fashion
        """
        nodes = self._nodes.values()
        for node in nodes:
            print(node)
            for child in node.children:
                out = " --- " + str(child)
                print(out)


class Node:

    """
    Tree helper class which stores individual node-related data.
    """

    def __init__(self, x, y, name, parent):
        # Cartesian x coordinate
        self.x = x
        # Cartesian y coordinate
        self.y = y
        # Node name. For Prim's should match graph node name
        self.name = name
        # parent Node object
        self.parent = parent
        # list of all child nodes
        self.children = set()

    def __str__(self):
        """
        Simple to-string method which prints the object data members
        """
        ret = "Node: " + str(self.name) + " x=" + str(self.x) + " y=" + str(self.y)
        return ret

