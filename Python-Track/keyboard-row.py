class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        res,dic=[],{}
        for idx,row in enumerate(rows):
            for ch in row:
                dic[ch]=idx

        for s in words:
            flag=False
            for i in range(len(s)-1):
                if dic[s[i].lower()]!=dic[s[i+1].lower()]: 
                    flag=True
                    break
            if flag==False: res.append(s)
        return res
        