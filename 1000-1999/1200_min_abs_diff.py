class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort array into order, then go through and iterate comparing to the next item
        arr.sort()

        min_diff_seen = float('inf')

        differences = defaultdict(list)
        for idx in range(len(arr) - 1):
            x, y = arr[idx], arr[idx+1]
            diff = abs(x - y)
            min_diff_seen = min(diff, min_diff_seen)
            if diff == min_diff_seen:
                differences[diff].append([x, y])

        return differences[min(differences)]
