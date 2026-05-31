class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # this is O(n logn) solution 

        nums =  sorted(nums)
        i = 1
        for n in nums:
            if n == i:
                i+=1
        return i

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