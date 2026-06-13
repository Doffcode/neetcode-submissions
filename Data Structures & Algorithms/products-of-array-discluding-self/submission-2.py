class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        parr = [1]*len(nums)
        for i,n in enumerate(nums):
            parr[i] = pre
            pre *= n
        suf = 1
        sarr = [1]*len(nums)
        for i in range (len(nums)-1, -1, -1):
            sarr[i] = suf
            suf*= nums[i]
        for i in range (len(nums)):
            sarr[i] *= parr[i]
        return sarr
