# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, stop = 1, n
        bad_version = float('inf')

        while start <= stop:
            midpoint = (start + stop) // 2
            if isBadVersion(midpoint):
                bad_version = min(midpoint, bad_version)
                stop = midpoint - 1
            else:
                start = midpoint + 1

        return bad_version

