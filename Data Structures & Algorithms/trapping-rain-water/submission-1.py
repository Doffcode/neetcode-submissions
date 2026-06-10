class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_bound = [0]*n
        cmax = 0
        for i,h in enumerate(height):
            left_bound[i] = cmax
            if h>cmax:
                cmax = h

        right_bound = [0]*n
        cmax = 0
        for i in range (n-1, -1 ,-1):
            right_bound[i] = cmax
            if height[i] > cmax:
                cmax = height[i]

                
        total = 0
        for l,r,h in zip(left_bound, right_bound, height):
            total += max (0, (min(l,r)-h))
        return total