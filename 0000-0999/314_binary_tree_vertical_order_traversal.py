from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = Queue()
        level.put((root, 0))

        next_level = Queue()
        columns = defaultdict(list)

        while not level.empty():
            node, column = level.get()
            columns[column].append(node.val)
            if node.left:
                next_level.put((node.left, column-1))
            if node.right:
                next_level.put((node.right, column+1))

            if level.empty() and not next_level.empty():
                level = next_level
                next_level = Queue()

        return [columns[i] for i in sorted(columns)]
