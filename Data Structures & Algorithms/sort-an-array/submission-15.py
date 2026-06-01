class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(nums):
            if len(nums)<2:
                return nums
            pivot = nums[(len(nums))//2]
            low = [x for x in nums  if x < pivot]
            mid = [x for x in nums  if x == pivot]
            high =[x for x in nums  if x > pivot]
            return qsort(low) + mid + qsort(high)

        nums = qsort(nums)    
        return nums