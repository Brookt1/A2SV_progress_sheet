class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        


        def find_num(target, pos):
            
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2

                if pos == 'last':
                    if nums[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid -1
            if pos == 'last':
                return right
            return left
        
        start = find_num(target, 'int')
        end = find_num(target, 'last')
        if -1 < start <len(nums) and nums[start] == target:
            return [start, end]

        return [-1, -1]