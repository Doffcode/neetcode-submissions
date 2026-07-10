class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l, r, csum = 0,0,0
        minlen = len(nums)
        while(r<len(nums)):
            csum+=nums[r]
            r+=1
            while(csum-nums[l] >= target):
                csum-=nums[l]
                l+=1
            if csum >= target:
                minlen = min(minlen,r-l)
        return minlen