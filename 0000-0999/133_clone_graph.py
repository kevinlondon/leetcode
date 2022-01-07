"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = {}
        return self.clone(node, nodes)

    def clone(self, node: 'Node', nodes: dict) -> 'Node':
        if not node:
            return

        if node.val in nodes:
            return nodes[node.val]

        nodes[node.val] = Node(val=node.val)
        nodes[node.val].neighbors = [self.clone(neighbor, nodes) for neighbor in node.neighbors]

        return nodes[node.val]
