class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mlen = mountainArr.length()
        #find the inflection point
        l = ind = 0
        r = mlen-1
        while(l<r):
            m = (l+r)//2
            left = mountainArr.get(m-1)
            right = mountainArr.get(m+1)
            mid = mountainArr.get(m)
            if left < mid < right:
                l=m
            elif left > mid > right:
                r= m+1
            else:
                ind = m-1
                break
        #search in left arr
        left = 0
        right = ind
        while(left<=right):
            mid = (left+right)//2
            if mountainArr.get(mid) < target:
                left = mid+1
            elif mountainArr.get(mid) > target:
                right = mid-1
            else:
                return mid
        left = ind+1
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