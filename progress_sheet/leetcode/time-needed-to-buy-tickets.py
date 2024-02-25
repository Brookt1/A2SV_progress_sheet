class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        que=deque(tickets)
        count=0
        while k>-1:
            if que[0]==1:
                if k==0:
                    break
                que.popleft()
            else:
                num=que.popleft()-1
                que.append(num)
            if k==0:
                k=len(que)-1
            else:
                k-=1
            count+=1
        return count+1




        