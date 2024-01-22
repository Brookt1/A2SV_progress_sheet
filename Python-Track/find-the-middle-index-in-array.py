class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix=[]
        sum=0
        for num in nums:
            sum+=num
            prefix.append(sum)
        for i in range(len(nums)):
            if i==0:
                if (prefix[-1]-prefix[i])==0:
                    return 0
            elif i==len(nums)-1:
                if prefix[i-1]==0:
                    return i
            elif prefix[-1]-prefix[i]==prefix[i-1]:
                return i
        return -1
            