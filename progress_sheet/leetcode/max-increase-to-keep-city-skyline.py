class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row=[]
        max_col=[0]*len(grid[0])

        for i in range(len(grid)):
            max_row.append(max(grid[i]))
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if max_col[j]<grid[i][j]:
                    max_col[j]=grid[i][j]
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans+=(min(max_col[i],max_row[j])-grid[i][j])
        return ans
        