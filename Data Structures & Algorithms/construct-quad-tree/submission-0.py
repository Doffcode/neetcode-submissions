"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 0: return None
        isleaf = True
        n = len(grid)
        val = grid[0][0]
        for i in range (n):
            for j in range (n):
                if grid[i][j] != val:
                    isleaf = False
                    break
        if isleaf == True:
            l = Node(val,True,None,None,None,None)
        else:
            m = n//2
            tl = self.construct([row[:m] for row in grid[:m]])
            tr = self.construct([row[m:n] for row in grid[:m]])
            bl = self.construct([row[:m] for row in grid[m:n]])
            br = self.construct([row[m:n] for row in grid[m:n]])
            l = Node(val,False,tl,tr,bl,br)
        return l