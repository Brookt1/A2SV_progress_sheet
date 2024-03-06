class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        nums = []
        for i in range(len(intervals)):
            nums.append([intervals[i][0],i])
        nums.sort()
        ans = []
        for start, end in intervals:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid][0] >= end:
                    right = mid - 1
                else:
                    left = mid + 1
            if left >= len(nums):
                ans.append(-1)
            else:
                ans.append(nums[left][1])
        return ans