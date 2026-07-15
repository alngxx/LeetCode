class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """ GCD(a, b) == GCD(b, a % b)
        1. Remainder shares same divisors as the original pair
        2. Repeat until remainder is 0
        """
        a = max(nums)
        b = min(nums)

        while b:
            a, b = b, a % b
        return a