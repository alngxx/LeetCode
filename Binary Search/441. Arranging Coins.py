class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        1. Brute force
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i-1
        2. Binary Search: O(log n)
        Find k largest satisfies: k(k+1)/2 <= n
        """
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            total = mid * (mid + 1) // 2

            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
