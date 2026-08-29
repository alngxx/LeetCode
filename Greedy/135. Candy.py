class Solution:
    def candy(self, ratings: List[int]) -> int:
        """ Greedy - Two Pass: O(n), O(1)
        1. Scan left-right: if a child's rating > left neighbor's, 
        set their candy count to one more than the left neighbor.

        2. Scan right - left: if a child's rating is higher than their right neighbor's, 
        set their candy count to the maximum of its current value and one more than the right neighbor.
        -> Take max to ensure not breaking the left condition
        """
        n = len(ratings)
        # every child get at least 1 candy
        res = [1] * n

        # left-to-right: satisfy left-neighbor condition
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        
        # 2. right-to-left: satisfy right-neighbor condition without breaking left condition
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i+1] + 1)
        
        return sum(res)