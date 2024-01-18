class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        res=float('inf')
        nums.sort()
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:

                sum=nums[i]+nums[left]+nums[right]
                if abs(target-res)>abs(target-sum):
                    res=sum
                if sum>target:
                    right-=1
                elif sum<target:
                    left+=1
                else:
                    return target
        return res
                
                


        