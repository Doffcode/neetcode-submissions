class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = sorted(Counter(nums).items(), key = lambda p:p[1], reverse = True)
        ret = []
        for i in range(k):
            ret.append(key[i][0])
        return ret