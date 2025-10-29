class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Hash map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        count = 0
        # If number i appear n times, count of its good pair is n*(n-1)/2
        for num in freq:
            count += freq[num] * (freq[num] - 1) // 2

        return count
