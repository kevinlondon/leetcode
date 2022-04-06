class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        Idea:
        * Initiate answer array with set for each
        * When encountering a new record, delete the previous one
        * Might be a way to save memory if we sort the array, but will be slower
        """

        users = defaultdict(set)
        answers = [0] * k

        for user, minute in logs:
            users[user].add(minute)

        for user, minutes in users.items():
            answers[len(minutes)-1] += 1

        return answers
