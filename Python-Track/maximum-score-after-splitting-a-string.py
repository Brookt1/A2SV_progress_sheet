class Solution:
    def maxScore(self, s: str) -> int:


        prefix=[0]
        total=0
        for i in range(len(s)):
            prefix.append(prefix[-1]+int(s[i]))
            total+=int(s[i])

        res=0
        for i in range(1,len(s)):
            res=max(res,i-prefix[i]+total-prefix[i])
        return res

        