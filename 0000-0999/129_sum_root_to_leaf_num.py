# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # idea: find children for each number.
        # multiply each number by the number of children plus self.
        # For example, 129, 123, 135 -> 100*3 + 20*2 + 30*1 + 9*1,
        # or, each child returns a stack with its own values. A list of stacks.

        allSums = self.sumSubtree(root)
        total = 0

        for stack in allSums:
            for i, val in enumerate(stack):
                total += val * 10**i

        return total

    def sumSubtree(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            children = [[root.val], ]
        else:
            children = self.sumSubtree(root.left) + self.sumSubtree(root.right)
            children = [stack + [root.val] for stack in children]

        return children

