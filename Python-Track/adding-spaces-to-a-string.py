class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        for idx, val in enumerate(spaces):

            if idx>0:
                res+=" "+s[spaces[idx-1]:val]
            else:
                res=s[:val]
        res+=' '+s[spaces[-1]:]
        return res

        