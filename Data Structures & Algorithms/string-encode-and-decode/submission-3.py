class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for s in strs:
            es += str(len(s))+"#"+s
        return es
    def decode(self, s: str) -> List[str]:
        ds = []
        left = 0
        while(left<len(s)):
            ind = s.find("#",left)
            lenght = int(s[left:ind])
            start = ind+1
            end = start +lenght
            ds.append(s[start:end])
            left = end
        return ds