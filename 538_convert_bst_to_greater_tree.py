# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    seen = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        self.convertBST(root.right)
        val = root.val
        root.val = self.seen = root.val + self.seen
        self.convertBST(root.left)
                
        return root