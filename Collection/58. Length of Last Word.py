class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        # Traverse backward
        # Break the loop whenever found space while already found a word (length > 0)
        for char in s[::-1]:
            if char != " ":
                length += 1

            elif char == "  " and length > 0:
                break

        return length
