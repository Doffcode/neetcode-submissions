class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(l,r):
            if l>=r:
                return nums
            p = nums[(l+r)//2]
            i = l
            j = r
            while(i<=j):
                while nums[i] < p :i+=1
                while nums[j] > p :j-=1
                if i<=j:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
                    j-=1
            qsort(l,j)
            qsort(i,r)
            return nums
        return qsort(0,len(nums)-1)