# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Idea:
        * Maintain a list of nodes to trim
        * Criteria for trimming include not having nodes of their own
        * When trimming, set parent directional node to None
        * Is there a more efficient way than iterating over the whole tree? Each time... Probably!

        [4,5], [2], [3]
        """

        leaves = []
        while root:
            child_leaves = []
            if not root.right and not root.left:
                leaves.append([root.val])
                break

            if root.left:
                left_leaves = self.findLeaves(root.left)
                root.left = None
            else:
                left_leaves = []

            if root.right:
                right_leaves = self.findLeaves(root.right)
                root.right = None
            else:
                right_leaves = []

            longest = max(len(right_leaves), len(left_leaves))
            for i in range(longest):
                right = right_leaves[i] if i < len(right_leaves) else []
                left = left_leaves[i] if i < len(left_leaves) else []
                leaves.append(left+right)

        return leaves
