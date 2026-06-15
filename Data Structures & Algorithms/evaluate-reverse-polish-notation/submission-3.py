class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operaters = ["+","-","/","*"]
        for tkn in tokens :
            if tkn in operaters:
                right = int(stack.pop())
                left = int(stack.pop())
                if tkn == "+":
                    stack.append(left+right)
                elif tkn == "-":
                    stack.append(left-right)
                elif tkn == "/":
                    stack.append(int(float(left/right)))
                else :
                    stack.append(left*right)
            else:
                stack.append(int(tkn))
        return stack[-1]