class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        seen = defaultdict(int)
        maxlen  = 0
        for i,c in enumerate(s):
            if c not in seen:seen[c] = i
            else :
                left = max(left,seen[c]+1)
                seen[c] = i
            maxlen = max(i - left + 1, maxlen)
            print(maxlen)
        return maxlen