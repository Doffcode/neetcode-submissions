class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x = point[0]
            y = point[1]
            if len(h) < k:
                heapq.heappush(h, (-(x*x+y*y), x ,y))
            else:
                heapq.heappushpop(h, (-(x*x+y*y), x ,y))
        return [[x,y] for _,x,y in h]