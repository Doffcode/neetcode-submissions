class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0 
        right = len(nums)-1
        i = 0
        def swap(l,r):
            nums[l],nums[r] = nums[r],nums[l]
        while(i<=right):
            if nums[i] == 0:
                swap(left,i)
                left+=1
            elif nums[i] == 2:
                swap(i,right)
                right-=1
                i-=1
            i+=1

        """
        Do not return anything, modify nums in-place instead.
        """
        