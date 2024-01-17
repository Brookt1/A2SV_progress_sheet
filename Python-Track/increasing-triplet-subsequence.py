class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min,mid=0,-1
        other_min=0
        for idx,val in enumerate(nums):
            if val<=nums[min]:
                if mid<0:
                    min=idx
                    other_min=idx
                elif val<nums[other_min]:
                    other_min=idx
                elif val>nums[other_min]:
                    mid=idx
                    min=other_min

            elif mid<0 or val<=nums[mid]:
                mid=idx
                min=other_min
            else:
                return True
        return False
    #[20,100,10,12,5,13]