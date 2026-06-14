class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            else:
                if stack:
                    if ((b == ")" and stack[-1] == "(") or 
                        (stack[-1] == "[" and b == "]") or
                        (stack[-1] == "{" and b == "}")):
                        stack.pop()
                    else :
                        return False
                else :
                    return False  
        if not stack :
            return True 
        else:
            return False
