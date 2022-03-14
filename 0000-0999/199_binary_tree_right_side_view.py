# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rightNodes = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        In-order traversal for each tier.
        Overwrite the record as we move to the right.
        """
        self.getRightMostNodes(root, depth=0)
        return self.rightNodes

    def getRightMostNodes(self, root: Optional[TreeNode], depth=0):
        if not root:
            return

        if len(self.rightNodes) < depth + 1:
            self.rightNodes.append(root.val)
        else:
            self.rightNodes[depth] = root.val

        self.getRightMostNodes(root.left, depth+1)
        self.getRightMostNodes(root.right, depth+1)
