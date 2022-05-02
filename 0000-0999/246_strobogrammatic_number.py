REVERSES = {
    '8': '8',
    '6': '9',
    '9': '6',
    '1': '1',
    '0': '0'
}

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        i = 0
        j = len(num)-1

        while i <= j:
            if num[i] != REVERSES.get(num[j]):
                return False

            i += 1
            j -= 1

        return True
