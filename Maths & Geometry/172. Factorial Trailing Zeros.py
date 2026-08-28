class Solution:
    def trailingZeroes(self, n: int) -> int:
        """ Factorial of 5: O(log5 n)
        Since each zero is 2*5, and we have plenty 2 
        just count how many factors of 5 are there
        """
        # 30 // 5 = 6 factors of 5
        # 6 // 5 = 1 factors of 5
        # 1 // 5 = 0 factors of 5
        # 30! has 7 trailing 0s
        count = 0
        while n > 0:
            count += n // 5
            n //= 5
        return count