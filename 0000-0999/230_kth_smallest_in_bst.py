# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import PriorityQueue

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        queue = PriorityQueue()
        self.getSmallest(root, k, queue)
        return -queue.get()

    def getSmallest(self, root: Optional[TreeNode], k: int, items: PriorityQueue):
        if not root:
            return

        items.put(-root.val)
        if items.qsize() > k:
            items.get()

        self.getSmallest(root.left, k, items)
        self.getSmallest(root.right, k, items)
