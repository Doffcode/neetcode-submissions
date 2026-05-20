class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        new_count = sorted(count.items(), key=lambda pair: pair[1], reverse = True)
        for i in range(k):
            res.append(new_count[i][0])
        return res