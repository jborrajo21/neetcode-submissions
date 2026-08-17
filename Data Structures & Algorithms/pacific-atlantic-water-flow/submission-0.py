class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(i,j):
            p,a = False, False
            visited = {(i,j)}
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                if x == 0 or y == 0:
                    p = True
                if x == len(heights) - 1 or y == len(heights[0]) - 1:
                    a = True
                if p and a:
                    return True
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and (nx,ny) not in visited and heights[nx][ny] <= heights[x][y]:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            return False
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs(i,j):
                    res.append([i,j])
        return res