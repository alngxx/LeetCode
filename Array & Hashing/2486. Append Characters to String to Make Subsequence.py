class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                # If found same char in both strings, move j forwards
                j += 1
            # Always move i forwards
            i += 1

        return len(t) - j
