class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict()
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        tmp = lastIndex[s[0]]
        res=[]
        init=-1
        for i , w in enumerate(s):
            if lastIndex[w]>tmp:
                tmp=lastIndex[w]
            if i==tmp:
                res.append(tmp- init)
                init=i
        return res
        


