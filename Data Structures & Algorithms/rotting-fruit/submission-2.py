class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs():
            final = 0
            while q:
                x,y,time = q.popleft()
                final = time
                for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        q.append((nx, ny, time + 1))
            return final

        
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                    q.append((i,j,0))
        
        time = bfs()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return time