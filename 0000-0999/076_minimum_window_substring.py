class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # could be duplicates in `t`

        # when adding a character of a type, look to see what the oldest of that type is
        # if it can be removed, do so. then look to see if that affects the longest / shortest item
        # maybe we use a priority queue?
        # no, just drop the oldest if it falls below the threshold for a given letter
        # then look for the lowest value among the ones remaining, that's your new lowest.

        # ADOBECODEBANC
        # A: 1, B: 4, C: 6
        # A: 1, B: 10, C: 6
        # A: 11, B: 10, C: 6
        # A: 11, B: 10, C: 12

        seen = defaultdict(list)
        desired = Counter(t)
        start, end = float('-inf'), float('inf')

        def is_valid():
            for letter, needed in desired.most_common():
                if not (letter in seen and len(seen[letter]) == needed):
                    return False

            return True

        for i, ltr in enumerate(s):
            if ltr in desired:
                if ltr in seen and len(seen[ltr]) == desired[ltr]:
                    seen[ltr].pop(0)

                seen[ltr].append(i)
                min_index = float('inf')
                if is_valid():
                    for letter, occurences in seen.items():
                        min_index = min(min_index, occurences[0])

                    if end - start > i - min_index:
                        start, end = min_index, i

        if start == float('-inf'):
            return ''
        return s[start:end+1]

