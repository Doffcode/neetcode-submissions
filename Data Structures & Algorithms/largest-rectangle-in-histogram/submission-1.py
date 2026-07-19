class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] #pair(index,height)
        for i,h in enumerate(heights):
            ind = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxarea = max(maxarea, (i-ind) * height)
            stack.append((ind,h))
        for i,h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))
        return maxarea