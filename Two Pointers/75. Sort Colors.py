class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = -1  # index of last red, init = None
        u = 0  # index of current unchecked element, init = start
        b = len(nums)  # index of first blue, init = end

        while u < b:
            # If current element is red, swap to the end of "red region". Then move forwards to next unchecked element
            if nums[u] == 0:
                r += 1
                nums[u], nums[r] = nums[r], nums[u]
                u += 1

            # If current element is white, leave it and move forward
            elif nums[u] == 1:
                u += 1

            # Else, current element is blue, swap it to the end of "blue region"
            else:
                b -= 1
                nums[u], nums[b] = nums[b], nums[u]
                # Do not increment u since swapped element need to be checked

        return nums
