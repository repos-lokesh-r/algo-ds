"""
Adjacency list representation of the graph
"""

from enum import Enum

class GraphType(Enum):
    UNDIRECTED = 1
 
# A class to represent the adjacency list of the node
 
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
 
 
# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices, graph_type):
        self.V = vertices
        self.graph = [None] * self.V
        self.graph_type = graph_type
 
    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Adding the source node to the destination as
        # it is the undirected graph
        if(graph_type == GraphType.UNDIRECTED):
            node = AdjNode(src)
            node.next = self.graph[dest]
            self.graph[dest] = node
 
    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
 