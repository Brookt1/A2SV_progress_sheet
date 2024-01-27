class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        prefix=[0]
        res=0
        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for i in range(1,len(prefix)):
            if prefix[i]-k in dic:
                res+=dic[prefix[i]-k]
            dic[prefix[i]]=dic.get(prefix[i],0)+1
        return res



            
