class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_max = -math.inf
        min_val = math.inf
        for i in range(len(nums)-1, -1,-1):
            while stack and stack[-1] <nums[i]:
                second_max = max(second_max, stack.pop())
        
            if second_max > nums[i]:
                return True

            stack.append(nums[i])

        return False