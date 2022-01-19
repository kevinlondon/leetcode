from queue import Queue

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 0

        for num in list(nums):
            if num not in nums:
                continue

            subseq = set([num])
            low, high = num-1, num+1

            while low in nums:
                subseq.add(low)
                low -= 1

            while high in nums:
                subseq.add(high)
                high += 1

            nums -= subseq
            longest = max(longest, len(subseq))

        return longest
