class Solution:
    def getRow(self, rowIndex: int) -> List[int]:




        def helper(row):
            if row==0:
                return [0,1,0]
            
            prev_pascal=helper(row-1)
            pascal=[0]
            print(prev_pascal)
            for i in range(len(prev_pascal)-1):
                pascal.append(prev_pascal[i]+prev_pascal[i+1])
            pascal.append(0)
            return pascal
        ans=helper(rowIndex)[1:]
        return ans[:len(ans)-1]

        