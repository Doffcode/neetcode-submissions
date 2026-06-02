class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mele = nums[0]
        melec = 1
        for i in range (1,len(nums)):
            if nums[i] == mele:
                melec +=1
            else:
                melec -=1

            if melec == 0:
                mele = nums[i]
                melec =1
        return mele
        
        

        
        