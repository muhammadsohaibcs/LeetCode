class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices , reverse=True) ==prices:
            return 0
        buy =prices[0]
        profit = float("-inf")
        for i in range(1, len(prices)):
            if buy > prices[i-1]:
                buy = prices [i-1]
            if profit < prices[i]- buy:
                profit = prices[i]- buy
        return profit


        