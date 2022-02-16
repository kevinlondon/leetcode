class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        subarrays = 0
        prefix_sum = 0
        sums = defaultdict(int)
        # base case - for when we're exactly on the number
        sums[0] = 1

        for num in nums:
            prefix_sum += num

            subarrays += sums[prefix_sum-k]
            sums[prefix_sum] += 1

        return subarrays
