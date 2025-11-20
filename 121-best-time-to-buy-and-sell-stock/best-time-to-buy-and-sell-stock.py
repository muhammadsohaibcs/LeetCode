class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices , reverse=True) ==prices:
            return 0
        l =[]
        l.append(float("inf"))
        profit = float("-inf")
        for i in range(1, len(prices)):
            if l[-1] < prices[i-1]:
                l.append (l[-1])
            else:
                l.append (prices [i-1])
            profit =max(profit , prices[i]- l[i])
        return profit


        