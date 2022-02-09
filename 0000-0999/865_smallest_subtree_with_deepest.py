# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        level = [root]
        next_level = []
        deepest = []

        while level:
            node = level.pop()
            deepest.append(node)

            if node.left:
                node.left.parent = node
                next_level.append(node.left)

            if node.right:
                node.right.parent = node
                next_level.append(node.right)

            if not level and next_level:
                level = next_level
                deepest = []
                next_level = []

        if len(deepest) == 1:
            return deepest[0]

        parents = set()
        deepest_level = list(deepest)
        while deepest_level:
            node = deepest_level.pop()
            parents.add(node.parent)

            if not deepest_level:
                deepest_level = list(parents)
                if len(deepest_level) == 1:
                    return deepest_level[0]
                else:
                    parents = set()

