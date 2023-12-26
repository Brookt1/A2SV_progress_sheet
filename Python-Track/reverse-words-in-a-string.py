class Solution:
    def reverseWords(self, s: str) -> str:


        s=s.split()
        s.reverse()
        res=[]
        for word in s:
            word.lstrip()
            word.rstrip()
            res.append(word)
        return ' '.join(res)

        