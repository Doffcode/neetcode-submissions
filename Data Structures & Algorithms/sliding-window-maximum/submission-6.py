class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ret = []
        for i, n in enumerate (nums):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while dq and n > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            ret.append(nums[dq[0]])
        return ret[k-1:]