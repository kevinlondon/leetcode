# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], isInTree=False) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        if root.val == subRoot.val:
            matches_left = self.isSubtree(root.left, subRoot.left, isInTree=True)
            matches_right = self.isSubtree(root.right, subRoot.right, isInTree=True)
            if matches_left and matches_right:
                return True

        if isInTree:
            return False

        return self.isSubtree(root.left, subRoot, False) or self.isSubtree(root.right, subRoot, False)
