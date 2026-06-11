class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        last_index = 0
        curr_len = 0
        maxlen = 0
        for index ,char in enumerate(s):
            if char in seen:
                last_index = max(seen[char] + 1, last_index)
                print ("index of ", char, "updated form ", seen[char] , " to ",index)
                seen[char] = index
                curr_len = index - last_index + 1
                if curr_len > maxlen:
                    maxlen = curr_len
            else:
                seen[char] = index
                curr_len = index - last_index + 1
                if curr_len > maxlen:
                    maxlen = curr_len
                print (s[last_index: index+1],"---",curr_len)
        return maxlen
        