# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and left not in (p, q):
            return left
        
        if right and right not in (p, q):
            return right
        
        found_p = found_q = False
        
        if p in (root, left, right):
            found_p = True
            
        if q in (root, left, right):
            found_q = True
        
        if found_p and found_q:
            return root
        
        if found_p:
            return p
        
        if found_q:
            return q