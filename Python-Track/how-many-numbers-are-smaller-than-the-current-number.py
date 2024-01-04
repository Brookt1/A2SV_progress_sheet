class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        dic={}

        for idx,val in enumerate(sorted(nums)):
            if val not in dic:
                dic[val]=idx
        res=[]
        for num in nums:
            res.append(dic[num])
        return res

        