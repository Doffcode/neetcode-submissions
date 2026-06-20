class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpri = float("inf")
        maxpro = 0
        for n in prices:
            minpri = min(minpri,n)
            maxpro = max(maxpro, n - minpri)
        return maxpro