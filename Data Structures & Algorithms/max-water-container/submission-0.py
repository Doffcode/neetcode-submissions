class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxw = 0
        for i in range (len(heights)):
            for j in range (i+1,len(heights)):
                w = (j-i)*(min(heights[i] , heights[j]))
                maxw = max(w,maxw)
        return maxw
        