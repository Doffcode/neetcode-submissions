class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] +=1
            ret[tuple(key)] += [s]
        return list(ret.values())