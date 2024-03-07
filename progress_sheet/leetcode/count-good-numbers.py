class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(1e9 + 7)

        def pow(x, n):
            if n == 0:
                return 1
            
            temp = pow(x, n//2)

            if n % 2 ==0:
                return (temp * temp) % mod
            else:
                return (x * temp * temp) % mod

        return  int(pow(5, (n+1)//2) * pow(4, n//2) % mod)



