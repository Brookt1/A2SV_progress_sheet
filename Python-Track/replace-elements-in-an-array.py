class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        for idx,val in enumerate(nums):
            dic[val]=idx
        for idx,val in operations:
            dic[val]=dic[idx]
            del dic[idx]
        for key,val in dic.items():
            nums[val]=key
        return nums