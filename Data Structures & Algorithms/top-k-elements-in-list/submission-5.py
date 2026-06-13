class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ret = []
        scount = sorted(count.items(), key = lambda p:p[1] ,reverse = True)
        for i in range (k):
            ret.append(scount[i][0])
        return ret