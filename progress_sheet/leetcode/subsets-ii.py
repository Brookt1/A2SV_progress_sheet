class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        ans = []
        def helper(idx, path):
            if idx == len(nums):
                ans.append(path.copy())
                return
            
            path.append(nums[idx])
            helper(idx + 1, path)
            while idx +1  <len(nums) and nums[idx+1] == nums[idx]:
                idx +=1
            path.pop()
            helper(idx + 1 , path)
        helper(0, [])
        return ans

        