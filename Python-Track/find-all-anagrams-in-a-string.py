class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_dic=Counter(p)
        window_dic=defaultdict(int)
        left,right=0,0
        res=[]
        while right<len(s):
            window_dic[s[right]]+=1
            if right-left+1>=len(p):
                if window_dic == target_dic:
                    res.append(left)
                window_dic[s[left]]-=1
                if window_dic[s[left]]<1:
                    del window_dic[s[left]]
                left+=1
            right+=1
        return res