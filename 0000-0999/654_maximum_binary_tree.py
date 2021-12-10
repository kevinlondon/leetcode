# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        
        largest = largest_idx = None
        
        for idx, num in enumerate(nums):
            if not largest or largest < num:
                largest = num
                largest_idx = idx
                
        node = TreeNode(largest)
        node.left = self.constructMaximumBinaryTree(nums[:largest_idx])
        node.right = self.constructMaximumBinaryTree(nums[largest_idx+1:])
        return node