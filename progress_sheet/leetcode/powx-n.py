class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        memo={}
        def pow(x,n):
            if n<=1:
                return x
            if n in memo:
                return memo[n]

            if n%2!=0:
                memo[n]=pow(x,n//2)*pow(x,ceil(n/2))
            else:
                memo[n]=pow(x,n/2)*pow(x,n/2)

            return memo[n]
        
        if n<0:
            return 1/pow(x,abs(n))

        return pow(x,abs(n))