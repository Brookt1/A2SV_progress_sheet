class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        count=len(set(nums))
        left,res=0,0
        n=len(nums)
        visted=Counter()
        for right in range(n):
            if nums[right] not in visted:
                count-=1
            visted[nums[right]]+=1
            while count==0:
                res+=(n-right)
                visted[nums[left]]-=1
                if visted[nums[left]]<1:
                    count+=1
                    del visted[nums[left]]
                left+=1
        return res

        