class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ Intuition: O(m x n)
        - Only need to compare with the first string
        - Take strs[0] as standard
        """
        for i in range(len(strs[0])):
            for s in strs:
                # i == len(s): if hit the end of any tring
                if i == len(s):
                    # Return longest common prefix
                    return s[:i]

                # strs[0][i] != s[i]: or whenever found any different character
                elif strs[0][i] != s[i]:
                    return s[:i]

        return strs[0]
