class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        Each match eliminate 1 team
        Start with n teams. Stop when 1 team left
        => n - 1 matches
        """
        return n - 1
