class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r, ret= 0,0,0
        maxf = defaultdict(int)
        while  r<len(s):
            maxf[s[r]]+=1
            r+=1
            while r- l- max(maxf.values()) > k :
                maxf[s[l]]-=1
                l+=1
            ret = max(ret, r-l)
        return ret