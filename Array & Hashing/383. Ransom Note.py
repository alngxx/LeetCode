class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """ Single Hashmap: O(n + m), O(n)
        1. Count frequency of every letter in magazine
        2. For each letter in ransomNote, decrement its count
        3. If count goes below 0, magazine doesn't have enough — return False
        """
        count_magazine = {}
        for letter in magazine:
            count_magazine[letter] = count_magazine.get(letter, 0) + 1
        
        for letter in ransomNote:
            count_magazine[letter] = count_magazine.get(letter, 0) - 1
            if count_magazine[letter] < 0:
                return False
        
        return True