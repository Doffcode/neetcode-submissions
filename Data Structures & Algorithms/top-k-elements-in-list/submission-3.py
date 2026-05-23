class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key = lambda p:p[1], reverse =True)
        for i in range (k):
            ret.append(sorted_counts[i][0])
        return ret