class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mp = 0
        for i in range(1,len(prices)):
            mp += max(0,prices[i]-prices[i-1])
        return mp