"""
Module to allow working with ordered and unordered graphs
"""

class Node:
    """
    Models a node, stores a value and a list of nodes which are related to it
    """
    value = 0
    _graph = None

    @property
    def related_nodes(self):
        return self._graph.get_related(self)


class RelatedNodes:
    """
    Class to abstract relationship of a node.
    Implements a subset of the set class
    """

    def add(self):
        pass
        
    def remove(self):
        pass
    
    def __len__(self):
        pass

   
class Relations:
    """
    Store the relationships among all nodes for a given graph
    """
    relationships = {}

    def get_related(self, node):
        """Return all nodes related to `node`"""
        pass


class Graph:
    """
    Provides interface to work with graph
    """
    relations = None
    nodes = []
    def node_factory(self, value, related_nodes=[]):
        """Factory for creating a node with a given value and list of siblings"""
        pass
