Job = namedtuple('Job', ['start', 'end', 'profit'])

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([Job(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        startTimes = [job.start for job in jobs]

        @lru_cache(None)
        def dp(i):
            if i == len(jobs):
                return 0

            job = jobs[i]
            # So either we take the job and look for the next or we skip this one
            nextJob = bisect.bisect_left(startTimes, job.end)
            maxProfit = max(dp(i+1), job.profit + dp(nextJob))
            return maxProfit

        return dp(0)
