# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        low = min(p.val, q.val)
        hi = max(p.val, q.val)

        if low <= root.val <= hi:
            return root
        elif root.val < low:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
