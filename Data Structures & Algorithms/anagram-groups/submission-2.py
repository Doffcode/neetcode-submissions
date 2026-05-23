class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = [[]]
        map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            map[key].append(s)
        return list(map.values()) 