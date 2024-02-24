class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        i=0
        n=len(palindrome)
        while i<n and palindrome[i]=='a':
            i+=1
        
        if n==1:
            return ''
        elif i==n or i>0 and i<n-1 and palindrome[i-1]=='a' and palindrome[i+1]=='a':
            return palindrome[:n-1]+'b'
        else:
            return palindrome[:i]+'a'+palindrome[i+1:]
        