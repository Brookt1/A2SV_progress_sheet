class Solution:
    def characterReplacement(self, s: str, k: int) -> int:



        left=0
        res=0
        dic=defaultdict(int)

        for right in range(len(s)):
            dic[s[right]]+=1
            while sum(dic.values())-max(dic.values())>k:
                dic[s[left]]-=1
                if dic[s[left]]<1:
                    del dic[s[left]]
                left+=1
            res=max(res,right-left+1)
        return res





        