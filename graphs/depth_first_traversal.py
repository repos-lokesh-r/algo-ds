"""
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

Sample Input
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
Sample Output
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
"""
import unittest

class Node:
    
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, child):
        self.children.append(Node(child))
        return self

    def deapth_first_search(self, array):
        stack = [self]

        while stack:
            current_node = stack.pop()
            array.append(current_node.name)
            stack.extend(current_node.children[::-1])

        return array


# Recursive Solution
# class Node:
    
#     def __init__(self, name):
#         self.children = []
#         self.name = name

#     def add_child(self, child):
#         self.children.append(Node(child))
#         return self

#     def deapth_first_search(self, array):
#         stack = [self]

#         while stack:
#             current_node = stack.pop()
#             array.append(current_node.name)
#             stack.extend(current_node.children[::-1])

#         return array


class TestCase(unittest.TestCase):
    def test(self):
        graph = Node("A")
        graph.add_child("B").add_child("C").add_child("D")
        graph.children[0].add_child("E").add_child("F")
        graph.children[2].add_child("G").add_child("H")
        graph.children[0].children[1].add_child("I").add_child("J")
        graph.children[2].children[0].add_child("K")
        self.assertEqual(graph.deapth_first_search([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
        print("Tests Passed")


TestCase().test()