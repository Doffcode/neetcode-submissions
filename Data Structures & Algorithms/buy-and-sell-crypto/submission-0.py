class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cmax = 0
        sa = [0]*n
        for i in range (n-1, -1, -1):
            sa[i] = cmax
            if prices[i] > cmax:
                cmax = prices[i]
        #print (sa)
        maxi = 0
        for n, ma in zip (prices, sa):
            if ma - n > maxi:
                maxi = ma -n
        return maxi


