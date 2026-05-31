class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ret = []
        for n in count:
            if count[n] >(len(nums)//3):
                ret.append(n)
        return ret