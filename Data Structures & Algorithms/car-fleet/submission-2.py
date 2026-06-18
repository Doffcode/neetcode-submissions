class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = {}
        for index,pos in enumerate(position):
            p_s[pos] = speed[index]
        p_s = dict(sorted(p_s.items()))
        print(list((p_s.items())))
        time = []
        for key,value in p_s.items():
            time.append((target-key)/value)
        stack = []
        for i in range(len(time)-1, -1, -1):
            if not stack:
                stack.append(time[i])
            else:
                if stack[-1] >= time[i]:
                    continue
                else:
                    stack.append(time[i])
        return len(stack)