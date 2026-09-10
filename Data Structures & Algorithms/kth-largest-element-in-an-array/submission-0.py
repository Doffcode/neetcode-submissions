class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = nums
        heapq.heapify(hp)
        while len(hp) >  k:
            heapq.heappop(hp)
        return hp[0]