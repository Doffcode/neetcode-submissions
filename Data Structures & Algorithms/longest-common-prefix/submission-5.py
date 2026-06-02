class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ml = len (strs[0])
        cf  = ""
        for s in strs :
            ml = min(ml, len(s))

        for i in range (ml):
            flag = False
            for j in range (len(strs)):
                if strs[0][i] != strs[j][i]:
                    flag = True
            if flag == False:
                cf += strs[j][i]
            else:
                return cf
        return cf