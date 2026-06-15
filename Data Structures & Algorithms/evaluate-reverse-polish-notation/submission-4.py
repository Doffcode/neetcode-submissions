class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+" : lambda a,b : int(a+b),
               "-" : lambda a,b : int(a-b),
               "*" : lambda a,b : int(a*b),
               "/" : lambda a,b : int(a/b)} 
        for token in tokens :
            if token in ops:
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(ops[token](left,right))
                
            else:
                stack.append(int(token))
        return stack[-1]