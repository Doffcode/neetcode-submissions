class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i,j):
            s[i],s[j] = s[j], s[i]
        for i in range (len(s)//2):
            swap(i,len(s)-1-i)