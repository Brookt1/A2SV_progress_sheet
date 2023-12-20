class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        rev=0
        c=x
        while c:
            
            rev=rev*10+c%10
            c=c//10
        return x==rev

