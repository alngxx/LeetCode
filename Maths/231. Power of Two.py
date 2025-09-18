class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powerofTwo = 1

        while powerofTwo <= n:
            if powerofTwo == n:
                return True
            powerofTwo *= 2

        return False
