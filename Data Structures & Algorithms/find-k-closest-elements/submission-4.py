class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = 0
        for i in range (len(arr)-k):
            if abs(arr[i+k]-x) < abs(arr[i]-x):
                ind = i+1
        return arr[ind:ind+k]