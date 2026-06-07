class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = min(len(word1),len(word2))
        newstr = ""
        for i in range (size):
            newstr += word1[i]+word2[i]
        return newstr + word1[size:] +word2[size:] 
