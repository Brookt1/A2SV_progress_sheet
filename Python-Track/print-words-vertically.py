class Solution:
    def printVertically(self, s: str) -> List[str]:

        s=s.split()
        n=max(len(x) for x in s)
        res=[]
        for i in range(n):
            a=''
            for j in range(len(s)):

                if i>=len(s[j]) and j<len(s)-1:
                    a+=" "
                elif i<len(s[j]): a+=s[j][i]
            res.append(a.rstrip())
        return res




        