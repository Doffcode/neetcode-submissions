class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if n <= 0:
                nums[i] = len(nums)+1
        for n in nums:
            if 1 <= abs(n) <= len(nums):
                nums[abs(n)-1] = -1 * abs(nums[abs(n)-1])
        print (nums)
        i = 1
        while (i <= len(nums)):
            if nums[i-1] < 0:
                i+=1
            else:
                return i
        return len(nums)+1
