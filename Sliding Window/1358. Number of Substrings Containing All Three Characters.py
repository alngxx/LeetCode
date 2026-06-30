class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """ Sliding Window: O(n), O(1) 
        1. Expand right, add s[r] to count
        2. While window has all 3 chars, shrink left and remove s[l] from count
        3. After shrinking, s[left - 1 ... right] is valid, thus s[0...right] also valid
        4. Add left to res
        """
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                count[s[left]] -= 1
                left += 1

            # loop breaks: s[left...right] is NOT valid 
            # so s[left-1...right] is smallest valid substring
            # thus s[0...right] are also valid substrings
            # thus, add "left" valid substrings from [0...left - 1] to res 
            res += left
        return res