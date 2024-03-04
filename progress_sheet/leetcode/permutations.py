class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(idx, path,arr):
            if idx == len(nums):
                ans.append(path.copy())
                return
            for i in range(0,len(arr)):
                path.append(arr[i])
                helper(idx + 1, path,arr[:i] + arr[i+1:])
                path.pop()

        helper(0,[], nums)
        return ans