# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        Ideas:
        * Find lowest common ancestor
        * Track path to lowest common ancestor with prefix
        * Or, just find the LCA and then iterate to find the value. Seems reasonable.
        * Binary tree isn't balanced
        """
        startPath, destPath = [], []
        self.findPathToNode(startValue, root, startPath)
        self.findPathToNode(destValue, root, destPath)

        while startPath and destPath and startPath[-1] == destPath[-1]:
            startPath.pop()
            destPath.pop()

        return ''.join('U' * len(startPath)) + ''.join(destPath[::-1])

    def findPathToNode(self, val, node, path):
        if not node:
            return False

        if node.val == val:
            return True

        if node.left and self.findPathToNode(val, node.left, path):
            path += 'L'
        elif node.right and self.findPathToNode(val, node.right, path):
            path += 'R'

        return path
