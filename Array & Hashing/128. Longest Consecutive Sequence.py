class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Hash set: O(n)
        Turn list -> set for O(1) lookups
        """
        set_nums = set(nums)
        # Initially, streak = 0
        streak = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                # num is the first number of the streak
                length = 1
                while (num + length) in set_nums:
                    length += 1
                    # Update longest streak only after current streak ends i.e while loop break
                streak = max(length, streak)

        return streak
