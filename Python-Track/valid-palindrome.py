class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=[]
        for ch in s:
            if ch.isalnum(): 
                if ch.isupper(): ss.append(ch.lower())
                else: ss.append(ch)
        l,r=0,len(ss)-1
        while l<r:
            if ss[l]!=ss[r]:
                return False
            l+=1
            r-=1
        return True

