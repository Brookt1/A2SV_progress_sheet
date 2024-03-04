class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def helper(idx, path, sum):

            if target == sum:
                ans.append(path.copy())
                return
            
            if sum > target or idx == len(candidates):
                return 
            
            path.append(candidates[idx])
            sum +=candidates[idx]
            helper(idx + 1, path, sum)
            sum -= path.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx +1]:
                idx +=1
            helper(idx + 1, path, sum)

        helper(0, [], 0)
        return ans

        