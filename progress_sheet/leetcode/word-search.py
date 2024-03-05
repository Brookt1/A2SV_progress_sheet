class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row,col = len(board), len(board[0])
        inbound = lambda r,c : -1 < r < row and -1 < c < col

        dir = [[1,0], [0, 1], [-1,0], [0, -1]]


        def helper(r, c, idx):
            if idx == len(word):
                return True
            
            if not inbound(r, c) or board[r][c] != word[idx]:
                return False
            board[r][c] = '#'
            for row, col in dir:
                if helper(r + row, c + col, idx + 1):
                    return True
            board[r][c] = word[idx]

            return False
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and helper(r,c,0):
                    return True
        
        return False



