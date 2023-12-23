class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        x,y=0,0
        for num in num1: 
            x=x*10+(ord(num)-ord('0'))
        for num in num2:
            y=y*10 + (ord(num)-ord('0'))
        return str(x*y)
        