class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        flag=False
        for i in range(1,n):
            
            if nums[i]<nums[i-1]:
                if flag: 
                    return False
                flag=True
                if i>1 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
        return True