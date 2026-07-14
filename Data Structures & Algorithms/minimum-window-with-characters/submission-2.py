class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        key = Counter(t)
        win = defaultdict(int)
        l,r,winlen = 0,0,float('inf')
        have,need = 0, len(key)
        bound = [-1,-1]

        while r < len(s):
            if s[r] in key:
                win[s[r]]+=1
                if win[s[r]] == key[s[r]]:
                    have += 1
            while have == need:
                if winlen > r-l+1:
                    winlen = r-l+1
                    bound = [l,r]
                if s[l] in key:
                    win[s[l]] -= 1
                    if win[s[l]] < key[s[l]]:
                        have -= 1
                l+=1
            r+=1
        l,r = bound
        return s[l:r+1]

