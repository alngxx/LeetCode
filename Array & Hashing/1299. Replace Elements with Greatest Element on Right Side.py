class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Intuition: O(n)
        - Update max_right as we scan backwards as the greatest element so far on the right
        - So we do not to scan twice to find max, which is O(n^2)
        """
        n = len(arr)
        res = [-1] * n
        max_right = -1

        # Scan array backwards from index [n-1] to [0], update max_right as we scan
        for i in range(n - 1, -1, -1):
            res[i] = max_right
            max_right = max(max_right, arr[i])

        return res
