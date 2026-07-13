class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # burte force
        ret = []
        for i in range (len(nums)-k+1):
            maxi = -float('inf')
            for j in range (k):
                maxi = max(maxi,nums[i+j])
            ret.append(maxi)
        return ret