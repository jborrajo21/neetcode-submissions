class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(x, y, idx):
            if idx == len(word) - 1:
                return board[x][y] == word[idx] 
            if board[x][y] != word[idx]:
                return False

            board[x][y] = '#'        
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if bt(nx, ny, idx + 1):
                        board[x][y] = word[idx]
                        return True
            board[x][y] = word[idx]    
            return False

        return any(bt(i, j, 0)
                for i in range(len(board))
                for j in range(len(board[0])))