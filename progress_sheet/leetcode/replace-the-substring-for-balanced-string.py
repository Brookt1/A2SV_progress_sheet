class Solution:
    def balancedString(self, s: str) -> int:
        count=Counter(s)
        print(count)
        dic={}
        for key,val in count.items():
            if val>len(s)//4:
                dic[key]=val-len(s)//4
        if not dic:
            return 0

        res=len(s)
        left=0
        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]]-=1
            while max(dic.values())<1:
                res=min(res,right-left+1)
                if s[left] in dic:
                    dic[s[left]]+=1
                left+=1
        return res