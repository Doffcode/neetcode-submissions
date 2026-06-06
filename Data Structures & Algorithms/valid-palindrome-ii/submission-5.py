class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        if s == s[::-1]:
            return True
        else:
            while(l < r):
                if (s[l] == s[r]):
                    l+=1
                    r-=1
                else:
                    sl = s[l+1:r+1]
                    sr = s[l:r]
                    return sl == sl[::-1] or sr[::-1] == sr
        return True

        