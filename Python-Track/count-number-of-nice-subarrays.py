class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        num_odd=0


        left=0
        right=0
        res=0
        n=len(nums)
        while right<n:
            if nums[right]%2!=0:
                num_odd+=1
            while num_odd==k:
                res+=1
                for i in range(right+1,n):
                    if nums[i]%2!=0:
                        break
                    res+=1
                if nums[left]%2!=0:
                    num_odd-=1
                left+=1
            right+=1
        return res