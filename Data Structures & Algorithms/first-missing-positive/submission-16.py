class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if n <= 0:
                nums[i] = len(nums)+1
        for n in nums:
            index = abs(n)-1
            if 0 <= index <= len(nums)-1:
                nums[index] = -1* abs(nums[index])
        print (nums)
        i = 1
        while (i <= len(nums)):
            if nums[i-1] < 0:
                i+=1
            else:
                return i
        return len(nums)+1
