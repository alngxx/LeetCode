class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        """
        Use HashMap to store frequency of each element
        Check if any element has frequency > 2: return False
        """
        freq = {}  # {num : freq}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] > 2:
                return False

        return True
