# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        value = 0
        if high >= root.val >= low:
            value += root.val

        if root.val < high:
            value += self.rangeSumBST(root.right, low, high)

        if root.val > low:
            value += self.rangeSumBST(root.left, low, high)

        return value
