class Solution:
    def totalMoney(self, n: int) -> int:

        sum,start=0,1
        for i in range(1,n+1):
            sum+=start
            if i%7==0:
                start=i//7
            start+=1
        return sum


        