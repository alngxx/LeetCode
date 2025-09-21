class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Intuition: Binary search -> O(logn)
        While L <= R:
            If mid² = target, return mid
            Elif mid² < target, search right half: L = mid + 1
            Else, search left half: R = mid - 1
            If x is not perfect square: Return R as largest integer while R² < x
        """

        L = 1  # (index 0)
        R = x  # (index len - 1)

        # Loop stops when L > R
        # Return R as the largest integer while R² < x
        while L <= R:
            mid = L + (R - L) // 2  # Avoid overflow if x too large

            square = mid * mid
            if square == x:
                return mid

            elif square < x:
                L = mid + 1

            else:
                R = mid - 1

        return R
