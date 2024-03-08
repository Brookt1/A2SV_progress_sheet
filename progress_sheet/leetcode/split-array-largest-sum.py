class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        left, right = max(nums), sum(nums)

        def splitter(val):
            part = 1
            _sum = 0
            for i in range(0, len(nums)):
                _sum += nums[i]
                if _sum > val:
                    part +=1
                    _sum = nums[i]
            return part
        
        while left <= right:
            mid = left + (right - left)//2
            part = splitter(mid)
            if part <= k:
                right = mid - 1
            else:
                left = mid + 1
        
        return left


