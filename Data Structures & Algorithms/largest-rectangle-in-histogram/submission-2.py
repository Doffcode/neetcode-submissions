class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        marea = 0
        st = []
        
        for i,h in enumerate(heights):
            start = i

            while st and st[-1][1] > h:
                ind, height = st.pop()
                marea = max(marea, height*(i-ind))
                start = ind
            st.append((start,h))
        
        for i,h in st:
            marea = max (marea, h*(len(heights)-i))
        return marea