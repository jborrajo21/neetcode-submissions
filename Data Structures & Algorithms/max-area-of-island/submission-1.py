class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != 1:
                return 0
            grid[x][y] = -1
            return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)

        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maximum = max(maximum, dfs(i, j))
        return maximum