class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def msort(l,m,h):
            if l == h:
                return nums[l:h+1]
            msort(l,(l+m)//2,m) 
            msort(m+1,(m+h)//2,h)
            left = nums[l:m+1]
            right = nums[m+1:h+1]
            i,j = 0,0
            ret = []
            while i<len(left) and j <len(right):
                if left[i] <= right[j]:
                    ret.append(left[i])
                    i+=1
                else:
                    ret.append(right[j])
                    j+=1
            ret += left[i:] +right[j:]
            nums[l:h+1] = ret
            return nums
        return msort(0,len(nums)//2,len(nums))
