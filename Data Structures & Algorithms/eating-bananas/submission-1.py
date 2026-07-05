class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sum = right = 0
        for n in piles:
            sum+=n
            right = max(right,n)
        left = math.ceil(sum/h)
        ret = 0
        while(left<=right):
            s1 = 0
            mid = (left+right)//2
            for n in piles:
                s1 += -(n//-mid)
            if s1<=h:
                ret = mid
                right = mid-1
            else:
                left = mid+1
        return ret