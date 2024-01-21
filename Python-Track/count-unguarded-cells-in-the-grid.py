class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matr=[[1]*n for _ in range(m)]
        for i,j in walls:
            matr[i][j]=-1
        for i,j in guards:
            matr[i][j]=-2
        
        for i,j in guards:
            #upward
            r=i-1
            while r>-1:
                if matr[r][j]==-1 or matr[r][j]==-2:
                    break
                matr[r][j]=0
                r-=1
            #downward
            r=i+1
            while r<m:
                if matr[r][j]==-1 or matr[r][j]==-2:
                    break
                matr[r][j]=0
                r+=1
            # To right
            c=j+1
            while c<n:
                if matr[i][c]==-1 or matr[i][c]==-2:
                    break
                matr[i][c]=0
                c+=1
            # To left
            c=j-1
            while c>-1:
                if matr[i][c]==-1 or matr[i][c]==-2:
                    break
                matr[i][c]=0
                c-=1
        res=0
        for i in range(m):
            for j in range(n):
                if matr[i][j]>0:
                    res+=1
        return res

        