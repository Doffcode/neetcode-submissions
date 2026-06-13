class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(l,r):
            nums[l],nums[r] = nums[r],nums[l]

        low = 0
        high = len(nums)-1
        i = 0
        while(i <= high):
            if nums[i] == 0:
                swap (i,low)
                low +=1
            if nums[i] == 2:
                swap(i,high)
                high-=1
                i-=1
            i+=1
        return nums


        