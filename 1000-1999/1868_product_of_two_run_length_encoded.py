class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def multiply(arr1, arr2):
            out = []

            i, j = 0, 0
            ir, jr = 0, 0
            while i < len(arr1):
                iv = arr1[i][0]
                jv = arr2[j][0]
                if ir == 0:
                    ir = arr1[i][1]
                if jr == 0:
                    jr = arr2[j][1]

                length = min(ir, jr)
                out.append([iv*jv, length])
                ir -= length
                jr -= length

                if ir == 0:
                    i += 1
                if jr == 0:
                    j += 1
            return out

        def compress(arr):
            compressed = []

            for val, count in arr:
                if not compressed or compressed[-1][0] != val:
                    compressed.append([val, count])
                else:
                    compressed[-1][1] += count

            return compressed

        return compress(multiply(encoded1, encoded2))
