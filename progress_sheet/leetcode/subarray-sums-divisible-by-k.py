class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        dic={0:1}
        prefix=[0]
        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])

        res=0
        for i in range(1,len(prefix)):
            rem=prefix[i]%k 
            if rem in dic:
                res+=dic[rem]
            dic[rem]=dic.get(rem,0)+1
        return res

        