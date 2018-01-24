# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.pathSumRecurse(root, total, mustFind=False)
        
    def pathSumRecurse(self, root, total, mustFind=False):
        if not root:
            return 0
        
        paths = 1 if root.val == total else 0
        left = self.pathSumRecurse(root.left, total-root.val, True)
        right = self.pathSumRecurse(root.right, total-root.val, True)
        
        if not mustFind:
            left += self.pathSumRecurse(root.left, total)
            right += self.pathSumRecurse(root.right, total)
            
        return paths + left + right
        