class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(q, visited):
            while q:
                x,y = q.popleft()
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and (nx,ny) not in visited and heights[nx][ny] >= heights[x][y]:
                        q.append((nx,ny))
                        visited.add((nx,ny))
        p = {(0, y) for y in range(len(heights[0]))} | {(x, 0) for x in range(len(heights))}

        a = {(len(heights) - 1, y) for y in range(len(heights[0]))} | {(x, len(heights[0]) - 1) for x in range(len(heights))}
        
        bfs(deque(p),p)
        bfs(deque(a), a)
        
        return list(p & a)