class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        


        seeker,holder=0,0
        while seeker<len(nums) and holder<len(nums):

            if nums[holder]!=val:
                holder+=1
            elif seeker<=holder or nums[seeker]==val:
                seeker+=1
            else:
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
        return holder

            
            
