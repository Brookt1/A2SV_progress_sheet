class Solution:
    def sortSentence(self, s: str) -> str:
        
        s=s.split()
        res=[]
        print(s)
        for word in s:
            res.append([word[-1],word[:len(word)-1]])
        res.sort()
        return ' '.join(word[1] for word in res)
        