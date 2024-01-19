class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum=0
        right_sum=0
        n=len(cardPoints)
        for i in range(k):
            left_sum+=cardPoints[i]
            right_sum+=cardPoints[n-i-1]
        left,right=0,n-1
        res=0
        for i in range(k):
            print(left_sum,right_sum)
            if left_sum>right_sum:
                res+=cardPoints[left]
                left_sum-=cardPoints[left]
                right_sum-=cardPoints[n-(k-left)]
                left+=1
            else:
                res+=cardPoints[right]
                right_sum-=cardPoints[right]
                left_sum-=cardPoints[k-(n-right)]
                right-=1
        return res