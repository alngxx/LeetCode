class Solution:
    def reverse(self, x: int) -> int:
        # Handle sign
        sign = -1 if x < 0 else 1

        # Make x positive for easier reversing
        # Initialize res = 0: res is the reversed integer without sign
        x = abs(x)
        res = 0

        while x:
            mod = x % 10  # Extract last digit
            x = x // 10  # Remove last digit

            # Build reversed integer
            res = res * 10 + mod

            # Ensure reversing do not exceed 32-bit range
            if res > 2 ** 31 - 1:
                return 0

        return sign * res
