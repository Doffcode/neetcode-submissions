class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ret = [0]*(len(temp))
        for i in range (len(temp)-1, -1, -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]-i
            stack.append(i)
        return ret