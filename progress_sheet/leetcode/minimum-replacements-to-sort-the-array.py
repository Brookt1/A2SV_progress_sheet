class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        

        answer=0
        prev_min=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>prev_min:
                number_of_elem=ceil(nums[i]/prev_min)
                answer+=number_of_elem-1
                prev_min=nums[i]//number_of_elem
            else: 
                prev_min=nums[i]
        return answer