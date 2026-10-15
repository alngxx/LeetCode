class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """ Greedy - track two candidates: O(n), O(1)
        1. first = smallest value seen so far
        2. second = second smallest value seen so far
        3. If we ever see any number > second, return True
        """
        first = second = float('inf')

        for n in nums:
            # if n <= first, it becomes first
            if n <= first:
                first = n
            # elif n > first but < second, it becomes second
            elif n <= second:
                second = n
            # else if n > second > first, triplet exists
            else:
                return True
        return False        