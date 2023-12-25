class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        dic={}
        for s in paths:
            s=s.split()
            for i in range(1,len(s)):
                idx=s[i].index('.')
                txt=s[i][idx+5:-1]
                if txt in dic: dic[txt].append(s[0]+'/'+s[i][:idx]+'.txt')
                else: dic[txt]=[s[0]+'/'+s[i][:idx]+'.txt']
        res=[]
        for key,val in dic.items():
            if len(val)>1:res.append(val)

        return res
