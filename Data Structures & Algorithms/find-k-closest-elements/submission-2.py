class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        darr=[]
        for n in arr:
            darr.append(abs(x-n))
        ind = 0
        s = sum(darr[:k])
        for i in range (len(arr)-k):
            cs = s-darr[i]+darr[i+k]
            if cs < s:
                s=cs
                ind = i+1
        ret = arr[ind:ind+k]
        return ret