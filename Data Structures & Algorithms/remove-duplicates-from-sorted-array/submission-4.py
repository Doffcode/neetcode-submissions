class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 1
        while (i<len(nums)):
            if nums[k] != nums [i]:
                print ("i = ",i,"  k= ",k)
                k+=1
                nums[k] = nums[i]
            i+=1  
        return k+1