# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = Queue()
        next_level = Queue()

        level.put(root)

        if not root:
            return 0

        max_level = 1

        while not level.empty():
            node = level.get()
            if not node:
                continue

            if node.left: next_level.put(node.left)
            if node.right: next_level.put(node.right)

            if level.empty() and not next_level.empty():
                level = next_level
                max_level += 1
                next_level = Queue()

        return max_level
