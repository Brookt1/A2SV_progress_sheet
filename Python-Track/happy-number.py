class Solution:
    def isHappy(self, n: int) -> bool:
        dic={}
        while n>1:
            if n in dic: return False 
            dic[n]=n
            s=str(n)
            n=0
            for num in s:
                n+=int(num)**2
        return True
        