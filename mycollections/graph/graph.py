"""
Module to allow working with ordered and unordered graphs
"""

class Node:
    """
    Models a node, stores a value and a list of nodes which are related to it
    """
    value = 0


class Relations:
    """
    Store the relationships among all nodes for a given graph
    """
    relationships = {}


class Graph:
    """
    Provides interface to work with graph
    """

    def node_factory(self, value, related_nodes=[]):
        pass
