class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, csum = 0, 0, 0
        minlen = len(nums)+1
        while r < len(nums):
            csum+= nums[r]
            r+=1
            while csum >= target:
                minlen = min(minlen, r-l)
                csum -= nums[l]
                l+=1
        if minlen == len(nums)+1:
            return 0
        else: return minlen