class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        last_level = [[i] for i in range(1, n+1)]
        level = []

        for _ in range(1, k):
            for val in last_level:
                for i in range(val[-1]+1, n+1):
                    level.append(val + [i])

            last_level = level
            level = []

        return last_level
