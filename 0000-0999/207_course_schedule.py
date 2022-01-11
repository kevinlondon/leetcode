from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        can_take = [0 for course in range(numCourses)]

        for course, requirement in prerequisites:
            prereqs[course].append(requirement)

        def dfs(course):
            if can_take[course] == -1:
                # We've seen it but haven't resolved so there's a cycle.
                return False
            elif can_take[course] == 1:
                # We've seen it, we know it can be taken.
                return True

            can_take[course] = -1
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            can_take[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
