# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        level = Queue()
        level.put(root)
        next_level = Queue()
        in_order = []
        level_in_order = []

        while not level.empty():
            node = level.get()
            level_in_order.append(node.val)
            if node.left: next_level.put(node.left)
            if node.right: next_level.put(node.right)

            if level.empty() and not next_level.empty():
                level = next_level
                next_level = Queue()
                in_order.append(level_in_order)
                level_in_order = []

        in_order.append(level_in_order)

        return in_order
