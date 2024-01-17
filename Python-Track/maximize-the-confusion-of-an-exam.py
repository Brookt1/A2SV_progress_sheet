class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        

        left=0
        dic={'T':0,'F':0}
        res=0
        for right in range(len(answerKey)):
            dic[answerKey[right]]+=1
            while min(dic.values())>k:
                dic[answerKey[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res

