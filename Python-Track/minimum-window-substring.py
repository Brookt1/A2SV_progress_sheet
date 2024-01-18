class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #I used the dynamic sliding window technique to solve the problem
        
        t_count=Counter(t)
        left,right=0,0
        res=''
        for right in range(len(s)):
            if s[right] in t_count:
                t_count[s[right]]-=1
            
            #reducing the size of the window if the window contain all char
            while max(t_count.values())<1:
                if len(res)==0 or len(res)>right-left+1:
                    res=s[left:right+1]
                if s[left] in t_count:
                    t_count[s[left]]+=1
                left+=1
        return res