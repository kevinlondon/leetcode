class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        l, r = 0, len(people)-1
        boats = 0

        while l <= r:
            left, right = people[l], people[r]
            if l == r:
                boats += 1
                l += 1
            elif left + right > limit:
                boats += 1
                r -= 1
            else:
                boats += 1
                l += 1
                r -= 1

        return boats
