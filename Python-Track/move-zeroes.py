class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        seeker,holder=1,0

        while seeker<len(nums) and holder<len(nums):
            if nums[seeker] and nums[holder]==0:
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
            elif nums[holder]:
                seeker=holder+1
                holder+=1
            else:
                seeker+=1