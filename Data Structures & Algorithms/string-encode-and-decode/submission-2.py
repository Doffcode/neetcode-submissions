class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_stirng = ""
        for s in strs:
            l = len(s)
            encoded_stirng += str(len(s))+"#"+s 
        return encoded_stirng
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        left = 0
        while(left<len(s)):
            index = s.find("#",left)
            lenght = int(s[left:index])
            start = index+1
            end = start + lenght
            decoded_string.append(s[start:end])
            left = end
        return decoded_string