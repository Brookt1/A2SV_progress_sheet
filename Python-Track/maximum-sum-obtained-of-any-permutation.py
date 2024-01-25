class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n=len(nums)
        prefix=[0]*(n)

        for start,end in requests:
            prefix[start]+=1
            if end+1<n:
                prefix[end+1]-=1
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        prefix.sort()
        nums.sort()
        res=0
        print(prefix)
        for i in range(n):
            res+=prefix[i]*nums[i]
        return res%(10**9+7)


        