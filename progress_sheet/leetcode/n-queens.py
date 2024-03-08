class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        board = [['.']*n for _ in range(n)]
        colums = set()
        forward_diag = set()
        backward_diag = set()


        ans = []
        def backtrack(row):
            if row == n:
                temp = []
                for r in board:
                    temp.append(''.join(r))
                ans.append(temp[:])
                return
            
            for col in range(n):
                if col not in colums and row - col not in backward_diag and row + col not in forward_diag:
                    forward_diag.add(row + col)
                    backward_diag.add(row -col)
                    colums.add(col)

                    board[row][col] = 'Q'

                    backtrack(row + 1)

                    forward_diag.remove(row + col)
                    backward_diag.remove(row -col)
                    colums.remove(col)

                    board[row][col] = '.'
        backtrack(0)
        return ans