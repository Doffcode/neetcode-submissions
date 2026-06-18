class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split("/")
        stack = []
        for d in dir:
            if d == "" or d == "." or (not stack and d == ".."):
                continue
            elif stack and d == "..":
                stack.pop()
            else:
                stack.append(d)
        print (stack)
        if not stack:
            return "/"
        fstr = ""
        for d in stack:
            fstr += "/"+d
        return fstr