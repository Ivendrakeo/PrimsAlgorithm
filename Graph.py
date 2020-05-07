"""
Authors: Draven Schilling, Andy Iliescu
Date: 5/7/20
Course: CS 3851 - Algorithms (Final Project)
"""

import sys


class WeightedGraph:
    """
    Implements a undirectional weighted graph structure.

    This implementation is NOT fully functional in that it is only meant
    to supplement a demonstration for Prim's Algorithm

 .
    """

    # Adjacency matrix  for the graph where
    # Key = Vertex obj and Value = set(Edge obj's)
    _edges = dict()
    # Set of all Vertex obj's
    _vertices = set()

    def __init__(self):
        self._edges = dict()
        self._vertices = set()

    def add_vertex(self, vertex):
        """
        Adds the given vertex to the WeightedGraph structure.
        Ensure this method is called alongside the add_edge() method
        such that there are no dangling vertex'es in the graph structure!
        """

    def add_edge(self, vertex_one, vertex_two):
        """
        TODO
        Populates the adjacency matrix by
        adding a connecting edge from vertex_one to vertex_two
        and an edge from vertex_two back to vertex_one.
        """
        pass

    def get_outgoing_edges(self, vertex):
        """
        TODO
        :param vertex: provided vertex
        :return: set() containing all edges from the provided vertex.
        """
        pass

    def remove_dangling_edges(self):
        """
         TODO
         Removes any isolated  vertex'es and edges
        """
        pass

    def remove_edge(self, edge):
        """
        TODO (may not do)
        Removes the desired edge from the graph. Ensures no dangling nodes
        are left within the graph. If there are, they are removed
        :param edge: edge object to be removed
        """

    @staticmethod
    def create_test_graph(x, y, num_vertices):
        """
        TODO
        Creates a test graph where all vertices fall within the (x,y) range
        and the number of edges connecting each vertex are sudo-random
        :param x: Graph plane width
        :param y: Graph plane height
        :param num_vertices: number of vertices to populate the graph with.
               must be less than the total area of the graph!
        :return: populated WeightedGraph
        """
        pass

    def _calculate_distance(self, x0, y0, x1, y1):
        """
        TODO
        Helper method which calculates the cartesian distance between
        two points on a plane
        :return: distance between points
        """
        pass


class Vertex:
    """
    Models Vertices in a WeightedGraph.
    The x and y coordinates are the cartesian coordinates where the vertex lies
    The name attribute is used for a unique identifier for each vertex.
    """
    def __init__(self, x, y, name):
        # Cartesian x coordinate
        self._x = x
        # Cartesian y coordinate
        self._y = y
        # Node name. For Prim's should match graph node name
        self._name = name
        # Denotes if the vertex has been visited for Prim's
        self._traversed = False

    def __str__(self):
        """
        TODO
        Simple to-string method which prints the object data members
        """
        pass


class Edge:
    """
    Models an Edge in a WeightedGraph.
    """

    def __init__(self, connectedVertex, distance):
        # Cartesian distance between vextex'es (distance)
        self._distance = distance
        # Vertex object which this edge connects to
        self._connectedVertex = connectedVertex

    def __str__(self):
        """
        TODO
        Simple to-string method which prints the object data members
        """
        pass
