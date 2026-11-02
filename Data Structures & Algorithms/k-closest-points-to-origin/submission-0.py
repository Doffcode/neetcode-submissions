class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point += [math.sqrt(point[0]*point[0] + point[1]*point[1])]
        points.sort(key = lambda p:p[2])
        ret = []
        for i in range (k):
            ret.append([points[i][0], points[i][1]])
        return ret