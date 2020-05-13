"""
Authors: Draven Schilling, Andy Iliescu
Date: 5/7/20
Course: CS 3851 - Algorithms (Final Project)
"""

import sys
import random
import math


class WeightedGraph:
    """
    Implements a undirectional weighted graph structure.

    This implementation is NOT fully functional in that it is only meant
    to supplement a demonstration for Prim's Algorithm

 
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
        :param vertex: vertex object
        :return True if successful. False otherwise
        """
        if vertex not in self._vertices:
            self._vertices.add(vertex)
            self._edges[vertex] = set()
            return True
        else:
            return False

    def add_edge(self, vertex_one, vertex_two):
        """
        Populates the adjacency matrix by
        adding a connecting edge from vertex_one to vertex_two
        and an edge from vertex_two back to vertex_one.
        Don't add an edge connecting a vertex to itself or
        an Edge that already exists
        :param vertex_one: vertex object connected by the edge
        :param vertex_two: other vertex object connected by the edge
        :return True if edge was successfully added. False otherwise
        """
        # Edge already exists flag
        found = False
        if vertex_one is not vertex_two:
            for item in self._edges[vertex_one]:
                if item.connectedVertex is vertex_two:
                    found = True
                    break
            if not found:
                self.add_vertex(vertex_one)
                self.add_vertex(vertex_two)
                d = self.calculate_distance(vertex_one, vertex_two)
                self._edges[vertex_one].add(Edge(vertex_two, d))
                self._edges[vertex_two].add(Edge(vertex_one, d))
                return True
        return False

    def get_outgoing_edges(self, vertex):
        """
        :param vertex: provided vertex
        :return: set() containing all edges from the provided vertex.
        """
        if vertex in self._vertices:
            return self._edges[vertex]
        else:
            return set()

    def get_starting_vertex(self):
        """
        Used in Prim's algorithm to define an arbitrary base vertex
        :return: some arbitrary vertex in the graph.
        """
        return next(iter(self._vertices))

    def remove_dangling_edges(self):
        """
         TODO (may not do)
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
        pass

    def print_graph(self):
        """
        Print's the graph to the console in a (somewhat)
        readable fashion
        """
        for vertex in self._vertices:
            print(vertex)
            for edge in self._edges[vertex]:
                print(edge)

    @staticmethod
    def create_test_graph(x, y, num_vertices):
        """
        Creates a test graph where all vertices fall within the (x,y) range
        and the number of edges connecting each vertex are sudo-random
        :param x: Graph plane width
        :param y: Graph plane height
        :param num_vertices: number of vertices to populate the graph with.
               must be less than the total area of the graph!
        :return: populated WeightedGraph. None if num_vertices is too large
        """
        if num_vertices > x*y:
            return None
        else:
            graph = WeightedGraph()  # create graph
            ver = set()  # set of used names
            objs = set()  # set of added vertex objects
            for i in range(0, num_vertices):
                success = False
                while not success:  # Keep trying to find a new vertex that's not already in the graph
                    x_rand = random.randrange(x)
                    y_rand = random.randrange(y)
                    point = str(x_rand) + str(y_rand)
                    if point not in ver:  # Once a new vertex has been found add it
                        success = True
                        working_vertex = Vertex(x_rand, y_rand, point)
                        graph.add_vertex(working_vertex)
                        # Add some connecting edges..
                        # Chose a random amount of vertices to add edges between
                        if i != 0:
                            num_edges = random.randrange(0, i)  # this might have to decay exponentially as i gets large
                            num_edges = 1 if (num_edges == 0) else num_edges
                            connecting_vertices = random.sample(objs, num_edges)
                            for vertex in connecting_vertices:
                                graph.add_edge(working_vertex, vertex)
                        # add vertex to local data
                        ver.add(point)
                        objs.add(working_vertex)
            return graph

    @staticmethod
    def calculate_distance(vertex_one, vertex_two):
        """
        TODO
        Helper method which calculates the cartesian distance between
        two vertexes in the graph using the standard distance formula
        :return: distance between vertexes
        """
        return math.sqrt((vertex_two.x-vertex_one.x)**2 + (vertex_two.y-vertex_one.y)**2)


class Vertex:
    """
    Models Vertices in a WeightedGraph.
    The x and y coordinates are the cartesian coordinates where the vertex lies
    The name attribute is used for a unique identifier for each vertex.
    """
    def __init__(self, x, y, name):
        # Cartesian x coordinate
        self.x = x
        # Cartesian y coordinate
        self.y = y
        # Node name. For Prim's should match graph node name
        self.name = name
        # Denotes if the vertex has been visited for Prim's
        self.traversed = False

    def __str__(self):
        """
        Simple to-string method which prints the object data members
        """
        res = "Vertex: " + str(self.name) + ", x=" + str(self.x) + ", y=" + str(self.y)
        return res


class Edge:
    """
    Models an Edge in a WeightedGraph.
    """

    def __init__(self, connectedVertex, distance):
        # Cartesian distance between vextex'es (distance)
        self.distance = distance
        # Vertex object which this edge connects to
        self.connectedVertex = connectedVertex

    def __str__(self):
        """
        Simple to-string method which prints the object data members
        """
        res = " --- " + str(self.connectedVertex.name)
        return res
