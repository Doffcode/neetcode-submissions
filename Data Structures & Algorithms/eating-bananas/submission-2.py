class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = -(sum(piles)// -h)
        right = max(piles)
        ans = right
        while(left <= right):
            mid = (left+right)//2
            hours_spent = sum(-(n//-mid) for n in piles)
            if hours_spent <= h:
                right = mid-1
                ans = mid
            else:
                left = mid+1
        return ans