class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.ans = []
        def helper(idx, arr):

            if idx == len(nums):
                self.ans.append(arr.copy())
                return
            arr.append(nums[idx])
            helper(idx+1, arr)
            arr.pop()
            helper(idx+1, arr)
        helper(0, [])
        return self.ans

        