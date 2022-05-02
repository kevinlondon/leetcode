class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        for j in range(1, len(arr) + k + 1):
            if i < len(arr) and arr[i] == j:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return j
