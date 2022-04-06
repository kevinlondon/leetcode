"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return False

        seen = set()

        node = p
        while node:
            seen.add(node)
            node = node.parent

        node = q
        while node:
            if node in seen:
                return node

            node = node.parent

