class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        cap = left
        while left <= right:
            i = s1 = 0
            mid = (left+right)//2
            no_of_days = 0
            while i < len(weights):
                while i < len(weights) and s1 + weights[i] <= mid :
                    s1+=weights[i]
                    i+=1
                no_of_days+=1
                s1 = 0
            if no_of_days <= days:
                right = mid-1
                cap = mid
            else:
                left = mid+1
        return cap

                