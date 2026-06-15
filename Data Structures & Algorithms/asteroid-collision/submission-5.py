class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if not stack:
                stack.append(n)
            else:
                if n > 0:
                    stack.append(n)
                else:
                    if stack[-1] < 0:
                        stack.append(n)
                    else:
                        while stack and stack[-1] > 0 and abs(stack[-1]) < abs(n):
                            stack.pop()
                        if stack and stack[-1] == abs(n):
                            stack.pop()
                        elif stack and stack[-1] < 0:
                            stack.append(n)
                        elif not stack:
                            stack.append(n)
        return stack