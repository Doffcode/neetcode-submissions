class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not list: return 0
        rows,cols = len(grid), len(grid[0])
        island = 0
        visited = set()

        def bfs (r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                ro,col = q.popleft()
                dir = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in dir:
                    r,c = ro+dr,col+dc
                    if (r in range(rows) and c in range (cols) and
                        grid[r][c] == '1' and
                        (r,c) not in visited):
                            visited.add((r,c))
                            q.append((r,c))
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island += 1
                    bfs(r,c)
        return island