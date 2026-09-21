class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def msort(l,m,r):
            if l >= r:return 
            msort(l, (l+m)//2, m)
            msort(m+1, (m+1+r)//2, r)
            left = nums[l:m+1]
            right = nums[m+1:r+1]
            ret = []
            i,j = 0,0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ret.append(left[i])
                    i+=1
                else:
                    ret.append(right[j])
                    j+=1
            ret+=(left[i:])+(right[j:])
            nums[l:r+1] = ret
            return 
        msort(0,len(nums)//2, len(nums)-1)
        return nums