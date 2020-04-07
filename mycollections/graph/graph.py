"""
Module to allow working with ordered and unordered graphs
"""

class Node:
    """
    Models a node, store a node and the relationship between other nodes
    as in a directed graphs (ie children and parensts)
    """
    value = 0
    _graph = None

    @property
    def parents(self):
        """Return RelationSet object for self's parents"""
        pass

    @property
    def children(self):
        """Return RelationSet object for self's children"""
        pass


class RelationSet:
    """
    Class to abstract relationship of a node.
    Implements a subset of the set class.
    Represents either a children set or parent set relationship
    """
    relations = set()
    map = None

    @classmethod
    def build_parent_relation(cls, node, map):
        """Return RelationSet for `node's` parent"""
        pass

    @classmethod
    def build_children_relation(cls, node, map):
        """Return RelationSet for `node's` children"""
        pass

    def add(self):
        pass
        
    def remove(self):
        pass
    
    def __len__(self):
        pass

    def __getitem__(self):
        pass

   
class Map:
    """
    Store the relationships among all nodes for a given graph
    """
    relationships = {} # (Node -> ([Node], [Node]))

    def add_parent(self, node, parent):
        """Add parent to node"""
        pass

     def add_child(self, node, child):
        """Add child to node"""
        pass

    def remove_parent(self, node, parent):
        """Remove parent from node"""
        pass

    def remove_child(self, node, child):
        """Remove child from parent"""
        pass

    

class Graph:
    """
    Provides interface to work with graph
    """
    relations = None
    nodes = []
    node_factory = lambda node, related_nodes : None

    def remove_node(self, node):
        """Remove node from graph and erase its relationships"""
        pass

    def union(self, graph):
        """Return Union of two graph objects"""
        pass

