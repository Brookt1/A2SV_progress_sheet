class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def dfs(idx,s):
            if idx>(len(s)-1)//2:
                return 
            dfs(idx+1,s)
            s[idx],s[len(s)-(idx+1)]=s[len(s)-(idx+1)],s[idx]
        dfs(0,s)
