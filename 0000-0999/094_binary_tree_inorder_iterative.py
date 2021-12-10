# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None a

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        current = root
        ans = []
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            ans.append(current.val)
            current = current.right
        
        return ans