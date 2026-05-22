class Solution:

        def encode(self, strs: List[str]) -> str:
            encoded_str =""
            for s in strs:
                pref = str(len(s))+"#"
                encoded_str += pref+s
            return encoded_str
        def decode(self, s: str) -> List[str]:
            ret = []
            i = 0
            while(i < len(s)):
                temp_len = ""
                while (s[i]!="#"):
                    temp_len +=s[i]
                    i+=1
                i+=1   
                l = int(temp_len)
                temp_str = ""
                for j in range (l):
                    temp_str += s[i]
                    i+=1
                ret.append(temp_str) 
            return ret
            