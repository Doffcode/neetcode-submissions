class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        for i in range(1,len(prices)):
            p = prices[i]-prices[i-1]
            if p>0:
                maxpro+=p
        return maxpro