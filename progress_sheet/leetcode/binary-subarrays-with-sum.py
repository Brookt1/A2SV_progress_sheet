class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        
        prefix=[]
        dic={0:1}
        for i in range(len(nums)):
            if prefix:
                prefix.append(prefix[-1]+nums[i])
            else:
                prefix.append(nums[i])
        res=0
        for i in range(len(prefix)):
            if prefix[i]-goal in dic:
                res+=dic[prefix[i]-goal]
            dic[prefix[i]]=dic.get(prefix[i],0)+1
        return res
            


