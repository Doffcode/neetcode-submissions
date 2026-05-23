class Solution:

        def encode(self, strs: List[str]) -> str:
            encoded_str =""
            for s in strs:
                encoded_str += str(len(s))+"#"+s
            return encoded_str
        def decode(self, s: str) -> List[str]:
            ret = []
            i = 0
            while (i<len(s)):
                j = s.find("#",i)
                lenght = int(s[i:j])
                print (lenght)
                start = j+1
                end = start+lenght
                ret.append(s[start:end])
                i=end
            return ret
            