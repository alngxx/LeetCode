class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Intuition
        - Two pointers i and j: i = 0; j = len - 1
        - i forwards and j backwards, skip non-alphanumeric chars
        - if found s[i].lower() != s[j].lower(): return False
        '''
        i = 0
        j = len(s) - 1

        while i < j:
            # Skip if non-alphanumeric
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            # If found one pair different -> not palindrome
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
