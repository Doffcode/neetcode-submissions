class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 :
                nums[i] = len(nums)+1
        for i in range (len(nums)):
            idx = abs(nums[i])-1
            if -1< idx < len(nums):
                nums[idx] = -1*abs(nums[idx])
        print (nums)
        for i in range(1,len(nums)+1):
            if nums[i-1] >0:
                return i
        return len(nums)+1