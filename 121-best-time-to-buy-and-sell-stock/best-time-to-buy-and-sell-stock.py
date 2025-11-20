class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices , reverse=True) ==prices:
            return 0
        buy =float("inf")
        profit = float("-inf")
        for i in range(1, len(prices)):
            if buy > prices[i-1]:
                buy = prices [i-1]
            profit =max(profit , prices[i]- buy)
        return profit


        