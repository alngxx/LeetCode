class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        # Loop through haystack
        for i in range(m):
            # Pointer k for needle
            k = 0
            # Pointer j in haystack
            for j in range(i, m):
                if haystack[j] == needle[k]:
                    k += 1
                # If found unmatched char, break, k reset to 0
                else:
                    break

                # If hit end of needle while match substring, return i
                if k == n:
                    return i
        return -1
