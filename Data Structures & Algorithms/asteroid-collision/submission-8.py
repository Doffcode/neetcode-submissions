class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if not stack or n > 0 or stack[-1] < 0:
                stack.append(n)
            else:
                while stack and stack[-1] < -n and stack[-1]>0:
                    stack.pop()
                if not stack or stack[-1] < 0 :
                    stack.append(n)
                elif stack[-1] == -n:
                    stack.pop()
        return stack