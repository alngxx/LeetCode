class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """ Sliding Window: O(n), O(1)
        1. Expand right, if s[r] is vowel, cur += 1
        2. If window.size > k, shrink left and cur -=1 if s[l] is vowel
        3. When window size == k, update res
        """
        vowel = 'aeiou'
        l = cur = res = 0
        
        for r in range(len(s)):
            if s[r] in vowel:
                cur += 1

            while r - l + 1 > k:
                if s[l] in vowel:
                    cur -= 1
                l += 1
            res = max(res, cur)

        return res