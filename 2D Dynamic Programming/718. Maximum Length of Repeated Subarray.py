class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """ Longest Common Subarray (2D DP): O(n*m), O(n*m)
        1. dp[i][j] = length of common subarray ending exactly at nums1[i-1], nums2[j-1]
        2. Match: dp[i][j] = dp[i-1][j-1] + 1
        3. Mismatch: dp[i][j] = 0 (mismatch means no common subarray ending at i-1 & j-1)
        4. Answer = max over the ENTIRE table, not dp[n][m]
        (the best subarray can end anywhere, not just at the last pair)
        """
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]      # (n + 1)(m + 1) array

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        
        res = 0
        for i in range(n + 1):
            for j in range(m + 1):
                res = max(res, dp[i][j])
        return res