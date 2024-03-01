class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n<1:
            return False
        ans = self.isPowerOfThree(n/3)
        return ans