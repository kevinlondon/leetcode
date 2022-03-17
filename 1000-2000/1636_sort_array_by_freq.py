class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_to_freq = Counter(nums)

        freq_to_num = defaultdict(list)
        for num, freq in num_to_freq.items():
            freq_to_num[freq].append(num)

        result = []
        for freq in sorted(freq_to_num.keys()):
            freq_nums = sorted(freq_to_num[freq], reverse=True)
            for freq_num in freq_nums:
                result += [freq_num] * freq

        return result
