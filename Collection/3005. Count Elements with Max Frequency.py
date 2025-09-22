class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}  # Dict to store freq of each element: {num : freq}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Max value in dict equal to the max frequency
        max_frequency = max(freq.values())

        total = 0

        # If frequency of any element = max_frequency, sum up its frequency
        for num in freq:
            if freq[num] == max_frequency:
                total += freq[num]

        return total
