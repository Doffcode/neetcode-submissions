class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # this is O(n logn) solution 

        # nums =  sorted(nums)
        # i = 1
        # for n in nums:
        #     if n == i:
        #         i+=1
        # return i

        # O(n) solution with O(n space)
        
        # seen = set(nums)
        # i = 1
        # while(i <= len(nums)):
        #     print (i)
        #     if i in seen:
        #         i+=1
        #     else:
        #         print ("the condition is false at i =",i)
        #         return i
        # return len(nums)+1

        #O(n) with constant space 

        for i in range( len(nums)):
            if nums[i]<0:
                nums[i] = 0

        for i in range (len(nums)):
            index = abs(nums[i])-1
            if -1<index<len(nums):
                if nums[index] != 0:
                    nums[index] = -1* abs(nums[index])
                else:
                    nums[index] = -1*(len(nums)+1)
            else:
                nums[i] = abs(nums[i])
        i = 1
        while(i<=len(nums)):
            if nums[i-1] < 0:
                i+=1
            else:
                return i
        return len(nums)+1

        