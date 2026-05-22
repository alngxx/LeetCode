class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Greedy approach: O(n) time, O(1) space
        Sum up all positive price increments between consecutive days.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
