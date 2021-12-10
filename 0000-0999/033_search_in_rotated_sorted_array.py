from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if target in nums else -1

        left_idx, right_idx = 0, len(nums) - 1

        while left_idx != right_idx and left_idx < len(nums) and right_idx > 0:
            mid_idx = (right_idx - left_idx) // 2 + left_idx
            left, mid, right = nums[left_idx], nums[mid_idx], nums[right_idx]

            print("Indices:", left_idx, mid_idx, right_idx)
            print("Numbers:", left, mid, right)

            if target == mid: return mid_idx
            if target == left: return left_idx
            if target == right: return right_idx

            if left < target < mid or (left > mid and (target < mid or target > left)):
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1

        return -1


sol = Solution()


def test_pivot_post_mid():
    seq = [4, 5, 6, 7, 0, 1, 2]
    assert sol.search(seq, 0) == 4


def test_single_item_missing():
    assert sol.search([1], 0) == -1


def test_first_item_is_result():
    assert sol.search([1], 1) == 0


def test_above_pivot():
    seq = [4,5,6,7,0,1,2]
    assert sol.search(seq, 1) == 5
