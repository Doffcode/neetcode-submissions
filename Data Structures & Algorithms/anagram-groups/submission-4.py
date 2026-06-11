class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        ans = []
        for s in strs:
            key = "".join(sorted(s))
            ret[key] += [s]
        return list(ret.values())