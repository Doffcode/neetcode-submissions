class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        cap = left
        while left <= right:
            s1 = 0
            mid = (left+right)//2
            no_of_days = 1
            for w in weights:
                if s1+w > mid:
                    s1 = w
                    no_of_days+=1
                else:
                    s1+=w
            if no_of_days <= days:
                right = mid-1
                cap = mid
            else:
                left = mid+1
        return cap

                