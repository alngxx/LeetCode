class Solution:
    def longestPalindrome(self, s: str) -> int:
        # dict store frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        res = 0
        has_odd_freq = False  # flag to check whether a character with odd frequency exists

        # Iterate through all frequencies
        for frequency in freq.values():
            if frequency % 2 == 0:
                res += frequency
            else:
                # If frequency of a character is odd, remove one of its occurence to remain palindrome.
                res += frequency - 1
                has_odd_freq = True
        # If there exists a character with odd frequency, we have at least one character
        # to make the center of an odd-length palindrome
        if has_odd_freq:
            return res + 1

        return res
