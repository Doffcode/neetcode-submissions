class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = ind = 0
        while l < len(arr)-k:
            if  abs(x-arr[l+k]) < abs(x-arr[l]):
                ind = l+1
            l+=1
        return arr[ind:ind+k] 

