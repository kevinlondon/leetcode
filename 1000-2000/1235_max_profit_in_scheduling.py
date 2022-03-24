class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        One idea is to decompose this to the maximum possible values at a given time,
        which is only possible when the time completes.
        We could sort by the max endTime and evaluate that.

        Maybe we need to track the overall max seen too?
        At each time, the maximum value will be either the max
        that we've seen so far or the value of the current time plus
        the max at the time we saw previously, right?
        """

        if not startTime:
            return 0

        Job = namedtuple('Job', ['start', 'end', 'profit'])

        jobs = [Job(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs = sorted(jobs, key=lambda x: x.end)

        max_time_profit = defaultdict(int)
        j_index = 0
        max_prof_seen = 0

        for i, job in enumerate(jobs):
            last_job = job
            j = i
            while j >= 0 and last_job.end > job.start:
                j -= 1
                last_job = jobs[j]

            if last_job.end <= job.start:
                max_prof_seen = max(max_prof_seen, max_time_profit[last_job.end]+job.profit)
            else:
                max_prof_seen = max(max_prof_seen, job.profit)

            max_time_profit[job.end] = max_prof_seen

        return max_prof_seen
