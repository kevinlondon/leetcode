class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        s = list(s)

        def replace(i):
            index = indices[i]
            source = sources[i]
            target = targets[i]

            for j, letter in enumerate(source):
                if index+j >= len(s) or s[index+j] != letter:
                    return

            s[index] = target
            for j in range(index+1, index+len(source)):
                s[j] = ''

        for i in range(len(indices)):
            replace(i)

        return ''.join(s)
