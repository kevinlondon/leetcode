class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        cursor = len(nums1) - 1

        while cursor >= 0:

            if (i >= 0 and j >= 0 and nums1[i] >= nums2[j]) or j < 0:
                val = nums1[i]
                i -= 1
            else:
                val = nums2[j]
                j -= 1

            nums1[cursor] = val
            cursor -= 1
