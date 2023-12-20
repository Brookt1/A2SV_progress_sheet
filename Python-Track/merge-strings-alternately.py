class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1,pt2=0,0
        res=''
        while pt1<len(word1) and pt2<len(word2):
            res+=word1[pt1]
            res+=word2[pt2]
            pt1+=1
            pt2+=1
        for i in range(pt1,len(word1)): res+=word1[i]
        for i in range(pt2,len(word2)): res+=word2[i]
        return res