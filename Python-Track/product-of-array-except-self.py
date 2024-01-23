class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        back_prefix,for_prefix=[1],[1]
        n=len(nums)
        for i in range(1,n+1):
            for_prefix.append(for_prefix[i-1]*nums[i-1])
        for i in range(n-1,-1,-1):
            back_prefix.append(back_prefix[n-i-1]*nums[i])
        back_prefix.append(1)
        back_prefix.reverse()
        res=[]
        for i in range(1,n+1):
            res.append(for_prefix[i-1]*back_prefix[i+1])
        return res
