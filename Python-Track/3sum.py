class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=set()
        n=len(nums)
        for i in range(n):
            l,r=i+1,n-1
            while l<r:
                if nums[i] + nums[l]+nums[r]==0:
                    if (nums[i] , nums[l],nums[r]) not in res:
                        res.add((nums[i] , nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[i] + nums[l]+nums[r]<0:
                        l+=1
                else:
                        r-=1
        return list(res)
        