class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = 1
        while power <= n:
            if power == n:
                return True
            power *= 4

        return False
