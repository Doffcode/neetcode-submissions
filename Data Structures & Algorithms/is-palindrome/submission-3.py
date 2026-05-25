class Solution:
    def isalpha (self, s:str) ->bool:
        if (ord("a") <= ord(s) <= ord("z") or
            ord("A") <= ord(s) <= ord("Z") or
            ord("0") <= ord(s) <= ord("9")):
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if (self.isalpha(c)):
                newstr+=c
        newstr = newstr.lower()
        i = 0
        j = len(newstr)-1
        while (i < j):
            #print ("i = ",newstr[i], " ", " j = ", newstr[j], "  " )
            if (newstr[i] == newstr[j]):
                i+=1
                j-=1
            else:
                return False 
        return True
        