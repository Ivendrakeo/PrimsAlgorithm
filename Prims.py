"""
Authors: Draven Schilling, Andy Iliescu
Date: 5/7/20
Course: CS 3851 - Algorithms (Final Project)
"""

import sys
import Graph
from Tree import Tree


def run_prims(graph, vertex):
    """
    TODO
    Run Prim's Algorithm to create a minimum spanning tree
    fram a weighted graph structure
    :param graph: populated WeightedGraph object
    :param vertex: vertex existing withing the WeightedGraph object
    :return: Tree Object representing the MSP of the WeightedGraph
    """
    # reset all the traversed flags
    for vertex in graph._vertices:
        vertex.traversed = False
    # setup result tree and add parent node
    t = Tree()
    t.add_node(None, vertex)
    vertex.traversed = True
    connected_edges = graph.get_outgoing_edges(vertex)
    # Greedily go find the next smallest edge until there is no edges left
    while len(connected_edges) > 0:
        #print("-----------")
        #for item in connected_edges:
        #    print(item)
        #    print(item.connectedVertex.traversed)
        smallest_dist = float("inf")
        smallest_edge = None
        # Find the next smallest un-traversed vertex
        for edge in connected_edges:
            if edge.connectedVertex.traversed is False and edge.distance < smallest_dist:
                smallest_dist = edge.distance
                smallest_edge = edge
        connected_edges.remove(smallest_edge)
        smallest_edge.connectedVertex.traversed = True
        # Update the connected edges set to include edges from the newly added vertex
        connected_edges = connected_edges | graph.get_outgoing_edges(smallest_edge.connectedVertex)  # set union
        t.add_node(smallest_edge.sourceVertex, smallest_edge.connectedVertex)
        # Remove other edges that end at the next smallest vertex.
        remove_set = set()
        for edge in connected_edges:
            if edge.connectedVertex.traversed is True:
                remove_set.add(edge)
        connected_edges = connected_edges - remove_set  # set difference
    return t


# test demo of Graph structure
# g = Graph.WeightedGraph.create_test_graph(100, 100, 10)
# g.print_graph()
# print("---------------------------------------------------------------------------------")
# t = run_prims(g, g.get_starting_vertex())
# t.print_tree()
