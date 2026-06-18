class Solution:
    def simplifyPath(self, path: str) -> str:
        # REMOVE THE EXTRA /
        newpath = ""
        for i in range (len(path)-1):
            if path[i+1] == "/" and path [i] == "/":
                continue
            newpath += path[i]
        #now put everything in stack
        #last index may be causing problem 
        if path[len(path)-1] != "/":
            newpath += path[len(path)-1]
        curname =""
        stack = []
        left = 1 
        while left < len(newpath):
            index = newpath.find("/",left)
            if index != -1:
                curname = newpath[left:index]
                stack.append(curname)
                left = index+1
            else:
                curname = newpath[left:]
                left = len(newpath)
                stack.append(curname)
                break
        newstack = []
        for s in stack:
            if s == "..":
                if newstack :
                    newstack.pop()
            elif s == ".":
                continue
            else:
                newstack.append(s)
        print(newstack)
        finalpath = ""
        if not newstack:
            return "/"
        for s in newstack:
            finalpath += "/"+s
        return finalpath
