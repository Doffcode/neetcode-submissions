class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ret = 0
        seen = defaultdict(int)
        for r in range (len(s)):
            seen[s[r]] += 1
            while r-l+1 - max(seen.values()) > k:
                seen[s[l]]-=1
                l+=1
            ret = max(ret, r-l+1) 
        return ret