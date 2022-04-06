# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest_values = []

        level = [root]
        next_level = []
        largest = float('-inf')

        while level:
            node = level.pop()
            if not node:
                continue

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            largest = max(largest, node.val)

            if not level:
                level = next_level
                largest_values.append(largest)
                largest = float('-inf')
                next_level = []

        return largest_values
