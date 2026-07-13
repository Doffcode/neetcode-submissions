class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mlen = mountainArr.length()
        #find the inflection point
        l = ind = 0
        r = mlen-1
        while(l<r):
            m = (l+r)//2
            if mountainArr.get(m-1)<mountainArr.get(m)<mountainArr.get(m+1):
                l=m
            elif mountainArr.get(m-1)>mountainArr.get(m)>mountainArr.get(m+1):
                r= m
            else:
                ind = m
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
            if mountainArr.get(mid) > target:
                left = mid+1
            elif mountainArr.get(mid) < target:
                right = mid-1
            else:
                return mid
        return -1