class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {")":"(" , "}":"{", "]":"[" }
        stack = []
        for char in s:
            if char not in brakets:
                stack.append(char)
            elif not stack or stack.pop() != brakets[char]:
                return False
        return not stack
