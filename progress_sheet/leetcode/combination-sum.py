class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:



        ans = []
        def helper(idx, path, sum):
            if sum == target:
                ans.append(path.copy())
                return
            if sum > target or idx == len(candidates):
                return
            
            path.append(candidates[idx])
            sum +=candidates[idx]

            helper(idx, path, sum)
            sum -= path.pop()
            helper(idx + 1, path, sum)

        helper(0, [], 0)
        return ans

        