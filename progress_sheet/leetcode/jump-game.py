class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jump=[0,nums[0]]
        for i in range(1,len(nums)):

            if i-jump[0]>jump[1]:
                return False
            if (jump[1]-(i-jump[0]))<=nums[i]:
                jump=[i,nums[i]]
        return True