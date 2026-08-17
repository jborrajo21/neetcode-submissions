class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,1))
        
        while q:
            x,y,d = q.popleft()
            for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx,ny = x + dx, y + dy
                if 0<=nx<len(grid) and 0 <=ny<len(grid[0]) and grid[nx][ny] > 0 and d < grid[nx][ny]:
                    grid[nx][ny] = d
                    visited.add((nx,ny))
                    q.append((nx,ny,d+1))
