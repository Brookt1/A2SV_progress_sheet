class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        res=''
        for i,ch in enumerate(strs[0]):
            for j in range(1,len(strs)):
                if strs[j][i]!=ch: return res
                    
            res+=ch
        return res