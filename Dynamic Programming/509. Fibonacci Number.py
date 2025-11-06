class Solution:
    def fib(self, n: int) -> int:
        """ DP - Bottom Up: O(n)
        a = F(n-2), init = F(0) = 0
        b = F(n-1), init = F(1) = 1
        We loop from 2 -> n and return b = F(n).
        If we loop from 1, it compute F(1) = F(-1) + F(0) -> Does not make sense
        """
        if n < 2:
            return n

        a, b = 0, 1  # F(0) = 0; F(1) = 1
        for i in range(2, n + 1):  # F(2) = F(0) + F(1)
            a, b = b, a + b
        return b
