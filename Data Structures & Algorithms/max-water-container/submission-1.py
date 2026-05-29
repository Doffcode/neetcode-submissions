class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mw = 0
        l = 0
        r = len(heights)-1
        while(l<r):
            w = (r-l) * (min(heights[r],heights[l]))
            mw = max(w, mw)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return mw
        