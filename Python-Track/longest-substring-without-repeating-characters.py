class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visted=set()
        l,r=0,0
        res=0
        while r<len(s):
            while s[r] in visted:
                visted.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            visted.add(s[r])
            r+=1
        return res
        