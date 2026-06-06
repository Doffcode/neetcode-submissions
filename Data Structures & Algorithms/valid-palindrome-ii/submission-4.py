class Solution:
    def p(self,s,l,r,count) -> bool:
        if l >r and count <=1: return True
        elif count  > 1:
            return False
        else:
            if s[l] == s[r]:
                print (s[l+1:r],count)
                return self.p(s,l+1,r-1,count) 
            else :
                print ("left = ",s[l:r] ," Right = ", s[l+1:r+1], count)
                return self.p(s,l,r-1,count+1) or self.p(s,l+1,r,count+1)
        return True

    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True
        else:
            return self.p(s,0,(len(s)-1),0) 
        return False