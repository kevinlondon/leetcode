from typing import List, Dict, Set, Tuple
from collections import defaultdict


from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
  nums = sorted(nums)
  solutions = []

  last_num = None
  for i in range(len(nums) - 2):
    a = nums[i]
    if last_num is not None and last_num == a:
      continue

    last_num = a
    if a > 0:
      break

    j, k = i + 1, len(nums) - 1

    while j < k:
      b, c = nums[j], nums[k]
      total = a + b + c
      if total == 0:
        solutions.append([a, b, c])

        while j < k and nums[j] == b:
          j += 1

        while j < k and nums[k] == c:
          k -= 1
      elif total > 0:
        k -= 1
      else:
        j += 1

  return solutions


def test_base_case():
    nums = [-1,0,1,2,-1,-4]
    assert threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]

def test_empty_case():
    assert threeSum([]) == []

def test_single_item():
    assert threeSum([0]) == []

def test_all_same_item():
    assert threeSum([0] * 1000) == [[0, 0, 0]]
