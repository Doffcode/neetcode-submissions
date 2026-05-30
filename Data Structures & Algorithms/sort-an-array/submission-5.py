class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left = arr[L : M+1]
            right = arr[M+1: R+1]
            i,j,k = 0, 0, L
            print(f"Before merge: arr[{L}:{R+1}] = {arr[L:R+1]}, left={left}, right={right}")
            while(i<len(left) and j<len(right)):
                if (left[i] <= right[j]):
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            while(i<len(left)):
                arr[k] = left[i]
                i+=1
                k+=1
            while(j<len(right)):
                arr[k] = right[j]
                j+=1
                k+=1

        def mergesort(arr,l,r):
            if l == r:
                return arr[l:r+1]
            m = (l+r)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            
            merge(arr, l, m, r)
            print(f"after merge: arr[{l}:{r+1}] = {arr[l:r+1]}")
            return arr

        return mergesort(nums,0,len(nums)-1)