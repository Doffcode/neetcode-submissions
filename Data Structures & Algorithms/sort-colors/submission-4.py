class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]
        
        left = 0                #last index which does not contain 0
        right = len(nums)-1     #last index that does not contain 2
        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(left,i)
                left +=1
            elif nums[i] == 2:
                swap(right,i)
                right-=1 
                i-=1
            i+=1



