class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(idx, i, j):
            if idx == len(word) - 1:
                return word[idx] == board[i][j]
            if word[idx] != board[i][j]: return False

            board[i][j] = '#'
            
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '#':                   
                    if bt(idx + 1, nx, ny):
                        return True
            board[i][j] = word[idx]
        
        return any(bt(0, i, j) for i in range(len(board)) for j in range(len(board[0])))