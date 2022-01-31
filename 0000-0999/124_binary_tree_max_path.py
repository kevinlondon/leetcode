# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0

            left = max(get_max_gain(node.left), 0)
            right = max(get_max_gain(node.right), 0)

            current_max_path = node.val + left + right
            max_path = max(max_path, current_max_path)

            return node.val + max(left, right)

        get_max_gain(root)
        return max_path
