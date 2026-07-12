class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        key, win, winlen = Counter(t), defaultdict(int), float('inf')
        l, r, have, wind, need = 0,0,0, [0,0], len(key)
        while r < len(s):
            c = s[r]
            if c in key :
                win[c]+=1
                if win[c] == key[c]:
                    have += 1
            while have == need:
                if  winlen > r-l+1:
                    wind = [l,r]
                    winlen = r-l+1
                if s[l] in key : 
                    win[s[l]] -= 1
                    if win[s[l]] < key[s[l]]:
                        have -= 1
                l+=1
            r+=1
        l,r = wind
        if winlen == float('inf'):
            return ""
        else:
            return s[l:r+1]