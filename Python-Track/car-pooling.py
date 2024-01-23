class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n=1001
        prefix=[0]*n
        for num,init,to in trips:
            prefix[init]+=num
            if to+1<n:
                prefix[to]-=num
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
            if prefix[i]>capacity:
                return False
        if prefix[0]>capacity:
            return False
        return True

        