class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic={}
        
        for i in range(len(mat)):
            
            for j in range(len(mat[0])):
                if i+j in dic:
                    dic[i+j].append(mat[i][j])
                else:
                    dic[i+j]=[mat[i][j]]
                              
        res=[]
        
        for i in range(max(dic.keys())+1):
            if i%2==0:
                res=res+ list(reversed(dic[i]))
            else:
                res=res+dic[i]
        return res
                              