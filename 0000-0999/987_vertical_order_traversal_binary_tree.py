# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(list))

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Implementation idea:
        * Build a dictionary with levels for each tier.
        * If no element at each tier, consider starting a new one.
        * x is divisible by 2 (if odd, offset by 0)
        * could also do a dictionary in dictionary,
        * probably less challenging, though requires sanitizing

        Runtime: O(n log n) - Dominated by sorting.
        """
        self.traverse(root, x=0, y=0)

        items = []

        for col in sorted(self.data.keys()):
            row_set = []
            for row in sorted(self.data[col]):
                row_set += sorted(self.data[col][row])

            items.append(row_set)

        return items

    def traverse(self, root, x, y):
        if not root:
            return

        self.data[y][x].append(root.val)
        self.traverse(root.left, x+1, y-1)
        self.traverse(root.right, x+1, y+1)
