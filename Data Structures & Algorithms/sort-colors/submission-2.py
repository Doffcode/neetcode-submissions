class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sfz = 0
        sft = len(nums)-1
        i = 0
        while(i <= sft):
            if nums[i] == 0 : 
                nums[i],nums[sfz] = nums[sfz],nums[i]
                sfz+=1
            if nums[i] == 2:
                nums[i],nums[sft] = nums[sft],nums[i]
                sft-=1
            else :
                i+=1


