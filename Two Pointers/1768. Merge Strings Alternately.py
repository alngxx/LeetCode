class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # This is quite similar to Mergesort!!
        res = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Append leftovers (only longer word)
        res.append(word1[i:])
        res.append(word2[j:])

        # Join the list into a string
        string = "".join(res)
        return string
