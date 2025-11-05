class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            # Index corresponds to this number (subtract 1 for 0-based indexing)
            i = abs(x) - 1

            # If number at that index is already negative
            # -> we've seen this number before
            if nums[i] < 0:
                res.append(i + 1)  # add the actual number
            else:
                nums[i] = -nums[i]  # otherwise, mark this number as seen

        return res
