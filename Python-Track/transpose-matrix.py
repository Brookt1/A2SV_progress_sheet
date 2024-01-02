class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for col in range(len(matrix[0])):
            temp=[]
            for row in range(len(matrix)):
                temp.append(matrix[row][col])
            res.append(temp)
        return res

        