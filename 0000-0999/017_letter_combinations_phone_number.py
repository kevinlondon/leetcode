MAP = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' '],
}

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        permutations = [""]
        for number in digits:
            current_permutations = []
            for letter in MAP[number]:
                current_permutations += ["{}{}".format(permutation, letter) for permutation in permutations]
            
            permutations = current_permutations
            
        return permutations if permutations != [""] else []
        