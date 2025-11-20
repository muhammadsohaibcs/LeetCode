class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        currSum = 0
        for i in nums:
            currSum += i
            if currSum > ans:
                ans = currSum
            if currSum <0 : currSum= 0 
        return ans