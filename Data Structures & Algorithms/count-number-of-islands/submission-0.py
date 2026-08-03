class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        q = deque()
        islands = 0

        def bfs():
            x, y = q.popleft()
            visited.add((x,y))
            for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1" and (nx, ny) not in visited:
                    q.append((nx, ny))
                    bfs() 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    q.append((i,j))
                    bfs()
                    islands += 1
        return islands

        
        