class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        q = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == "O":
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            i,j = q.popleft()
            for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                x,y = i + dx, j + dy
                if 0<=x<len(board) and 0 <=y<len(board[0]) and board[x][y] == "O" and (x,y) not in visited:
                    q.append((x,y))
                    visited.add((x,y))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited:
                    board[i][j] = "X"
