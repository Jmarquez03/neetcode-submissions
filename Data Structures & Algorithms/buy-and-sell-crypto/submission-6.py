class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while i < len(prices):
            j = i
            while j < len(prices) and prices[i] <= prices[j]:
                profit = max((prices[j] - prices[i]), profit)
                j += 1
            i = j
        return profit
