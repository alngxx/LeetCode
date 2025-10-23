class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """ Time Complexity: O(√c)
        c is sum of two squares
        iff the prime factorization of c,
        every prime of the form (4k+3) occurs an even number of times
        """
        i = 2  # First prime number
        while i * i <= c:
            count = 0
            while c % i == 0:
                count += 1  # count of current prime i.e. keep divide c by i until cannot
                c //= i

                # Check if i (current prime) is 4k+3 and i appears even times
            if i % 4 == 3 and count % 2 != 0:
                return False
            i += 1  # Move to next prime

        # c never % 4 == 3
        return c % 4 != 3
