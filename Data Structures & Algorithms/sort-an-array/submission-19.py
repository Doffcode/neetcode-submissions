class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(nums,low,high):
            i = low
            j = high
            if i>=j:
                return nums
            pivot = nums[(low+high)//2]
            while(i<=j):
                while(nums[i]<pivot):
                    i+=1
                while(nums[j]>pivot):
                    j-=1
                if i<=j:
                    nums[i],nums[j]  = nums[j],nums[i]
                    i+=1
                    j-=1
            qsort(nums,low,j) 
            qsort(nums,i,high)
            return nums
        nums = qsort(nums,0,len(nums)-1)    
        return nums