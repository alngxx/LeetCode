class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            # Whenver find an adjacent pair with same parity, return False
            if (nums[i] % 2) == (nums[i - 1] % 2):
                return False
        return True
