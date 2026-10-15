class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ Sliding Window: O(n), O(1)
        Variable window-size problems pattern:
        1. Slide right
        2. Check condition
        3. Shrink left
        4. Update res
        """
        l = 0
        res = 0

        for r in range(len(nums)):
            # 1. slide right: use a flip if encounter 0
            if nums[r] == 0:
                k -= 1

            # 2. check condition: if run out of flip
            while k < 0:
                # 3. shrink left: restore a flip if nums[l] is zero
                if nums[l] == 0:
                    k += 1
                l += 1
            
            # 4. update res
            res = max(res, r - l + 1)
        
        return res