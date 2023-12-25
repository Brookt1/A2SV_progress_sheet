class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic: dic[nums[i]]=[i]
            else: dic[nums[i]].append(i)
        for num in nums:
            va=target-num
            if va in dic: 
                if va==target//2:
                    if len(dic[va])>1: return dic[va]
                else:
                    return [dic[num][0],dic[va][0]] 


        