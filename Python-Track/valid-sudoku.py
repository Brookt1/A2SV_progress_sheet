class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visted=set()

        for row in board:
            visted.clear()
            for num in row:
                if num.isdigit():
                    if num in visted: 
                        return False
                    else: visted.add(num)
        
        for j in range(9):
            visted.clear()
            for i in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in visted : 
                        return False
                    else: visted.add(board[i][j])
        for i in range(0,9,3):
            for j in range(0,9,3):
                visted.clear()
                for y in range(3):
                    for x in range(3):
                        if board[i+y][j+x].isdigit():
                            if board[i+y][j+x] in visted: 
                                return False
                            else: visted.add(board[i+y][j+x])
        return True