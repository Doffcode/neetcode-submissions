class Solution:
    def trap(self, height: List[int]) -> int:
        left_bound = []
        left_bound.append(0)
        cmax = 0
        for n in height:
            if n > cmax:
                cmax = n
            left_bound.append (cmax)
        left_bound.pop()

        right_bound = []
        right_bound.append(0)
        cmax = 0
        for n in reversed(height):
            if n > cmax:
                cmax = n
            right_bound.append(cmax)
        right_bound.reverse()
        right_bound.pop()
        sum = 0
        for i in range (len(height)):
            sum += max(0,  (min(left_bound[i],right_bound[i])  -   height[i]))
        print (left_bound)
        return sum


        