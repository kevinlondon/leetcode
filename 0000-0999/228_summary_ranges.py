class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lower = None

        if not nums:
            return []

        ranges = []

        for i, num in enumerate(nums):
            if lower is None:
                lower = num
            else:
                last = nums[i-1]
                if num != last + 1:
                    if lower == last:
                        ranges.append(str(lower))
                    else:
                        ranges.append(f"{lower}->{last}")
                    lower = num


        if lower == nums[-1]:
            ranges.append(str(lower))
        else:
            ranges.append(f"{lower}->{nums[-1]}")

        return ranges
