class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:


        total,prefix=0,[0]
        n=len(nums)
        for i in range(1,n+1):
            prefix.append(prefix[-1]+nums[i-1])      
            total+=nums[i-1]
        res=[]
        for i in range(1,n+1):
            diff=nums[i-1]*(i-1)-prefix[i-1]+ total-prefix[i]-(n-i)*nums[i-1]
            res.append(diff)
        return res