class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Assume: n = 26
        => 3 full weeks + 5 remaining days = 135
        """
        week = n // 7
        day = n % 7
        # Sum of all full weeks: 28 + 35 + 42
        full_week = 28 * week + 7 * (week - 1) * week // 2

        # Add remaining days: 4 + 5 + 6 + 7 + 8
        remaining = sum(range(1, day + 1)) + week * day

        return full_week + remaining
