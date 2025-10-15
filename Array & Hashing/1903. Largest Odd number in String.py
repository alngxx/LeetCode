class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        # Scan backwards until find an odd digit, then return largest odd substring
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]

        return ""
