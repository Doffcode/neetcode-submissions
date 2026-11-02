class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        ret = []
        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(h, (x*x+y*y, x ,y))
        for i in range (k):
            d,x,y = heapq.heappop(h)
            ret.append([x,y])
        return ret