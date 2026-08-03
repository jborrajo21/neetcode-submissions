class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(x, y):
            grid[x][y] = "#"
            for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    dfs(nx, ny)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        
        return islands    