class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Brute force: O(sqrt(x)) -> Much slower than Binary Search
        if num == 1:
            return True

        i = 1
        while i*i < num:
            i += 1
            if i*i == num:
                return True

        return False
        """

        # Binary Search: O(logn)
        L = 1
        R = num
        # Loop stops when L > R but still can't find mid^2 == num
        # Thus, num is not perfect square -> Auto return False
        while L <= R:
            mid = L + (R - L) // 2  # Avoid overlow if num very large
            square = mid * mid

            # if found mid^2 == num, num is perfect square
            if square == num:
                return True

            elif square < num:
                L = mid + 1  # Search right half

            else:
                R = mid - 1  # Search left half

        return False
