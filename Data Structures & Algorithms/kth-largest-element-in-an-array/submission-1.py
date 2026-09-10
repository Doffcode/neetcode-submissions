class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        for n in nums[k:]:
            if n > hp[0]:
                heapq.heappush(hp,n)
                heapq.heappop(hp)
        return hp[0]