class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mlen = mountainArr.length()
        #find the inflection point
        l = ind = 0
        r = mlen-1
        while(l<r):
            m = (l+r)//2
            left = mountainArr.get(m)
            mid = mountainArr.get(m+1)
            if left < mid:
                l=m+1
            else:
                r = m
        #search in left arr
        left = 0
        right = r
        while(left<=right):
            mid = (left+right)//2
            num = mountainArr.get(mid)
            if num < target:
                left = mid+1
            elif num > target:
                right = mid-1
            else:
                return mid
        left = r+1
        right = mlen-1
        while(left<=right):
            mid = (left+right)//2
            num = mountainArr.get(mid)
            if num > target:
                left = mid+1
            elif num < target:
                right = mid-1
            else:
                return mid
        return -1