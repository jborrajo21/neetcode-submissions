class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = []
        def bt(idx, actions):
            for (x, y) in actions:
                if board[x][y] == word[idx]:
                    used.append((x,y))
                    if idx == len(word) - 1:
                        return True
                    
                    new_actions = []
                    for i in [1, -1]:
                        new_x = x + i
                        if new_x < 0 or new_x >= len(board): continue
                        cord = (new_x, y)
                        if cord not in used:
                            new_actions.append(cord)
                    for j in [1, -1]:
                        new_y = y + j
                        if new_y < 0 or new_y >= len(board[0]): continue
                        cord = (x, new_y)
                        if cord not in used:
                            new_actions.append(cord)

                    res = bt(idx+1, new_actions)
                    if res:
                        return True
            if used:
                used.pop()
            return False
        
        return bt(0, [(i, j) for i in range(len(board)) for j in range(len(board[0]))])