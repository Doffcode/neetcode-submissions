class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        ret = [n for n in nums]
        for i, n in enumerate(nums):
            ret[i] = pre
            pre *= n
        suf = 1
        for i in range(len(nums)-1,-1,-1):
            ret[i] *= suf
            suf *= nums[i]
        return ret