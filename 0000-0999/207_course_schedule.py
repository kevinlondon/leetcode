from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        can_take = [False for course in range(numCourses)]

        for course, requirement in prerequisites:
            prereqs[course].append(requirement)

        for course in range(numCourses):
            self.canTake(course, can_take, prereqs, seen=set())

        return all(can_take)

    def canTake(self, course: int, can_take: list, prereqs: defaultdict(list), seen: set) -> bool:
        required = deque([course])

        while required:
            prereq = required.popleft()

            if can_take[prereq]:
                continue
            elif prereq in seen:
                return False

            seen.add(prereq)

            requirements = prereqs[prereq]
            for requirement in requirements:
                if not self.canTake(requirement, can_take, prereqs, seen):
                    return False

        if not required:
            can_take[course] = True
            return True
