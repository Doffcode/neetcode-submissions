class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ""
        for c in s1:
            if c.isalnum():
                s2+=c
        print(s2,s2[::-1])
        return s2 == s2[::-1]
# ("a"<= c <="z") or (0<= int(c) <=9)