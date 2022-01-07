"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from queue import Queue

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        adjacency_list, nodes = {}, {}

        if not node:
            return

        self.buildNodes(node, nodes, adjacency_list)
        self.buildNeighbors(nodes, adjacency_list)

        return nodes[node.val]

    def buildNodes(self, node: 'Node', nodes, adjacency_list):
        adjacency_list[node.val] = [node.val for node in node.neighbors]
        nodes[node.val] = Node(val=node.val)

        for neighbor in node.neighbors:
            if neighbor.val not in adjacency_list:
                self.buildNodes(neighbor, nodes, adjacency_list)

    def buildNeighbors(self, nodes, adjacency_list):
        for value, neighbors in adjacency_list.items():
            nodes[value].neighbors = [nodes[neighbor] for neighbor in neighbors]

