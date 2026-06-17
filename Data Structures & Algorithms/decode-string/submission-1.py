class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0 
        curstr = ""
        curmul = ""
        finalstr = ""
        while (i < len(s)):
            if s[i] != "]":
                stack.append(s[i])
                i+=1
                print (stack)
            else:
                while(stack[-1] != "["):
                    curstr = stack.pop() + curstr
                stack.pop()
                while(stack and stack[-1].isdigit()):
                    curmul = stack.pop() + curmul
                stack.append(curstr*int (curmul))
                curmul = ""
                curstr = ""
                i+=1
        while stack:
            finalstr = stack.pop()+ finalstr
        return finalstr

