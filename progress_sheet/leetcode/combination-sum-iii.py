class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        

        ans = []
        def helper(val, path,sum):

            if len(path) == k:
                if sum == n:
                    ans.append(path.copy())
                return
            if sum > n: return

            for i in range(val, 10):
                path.append(i)
                helper(i + 1, path,sum + i)
                path.pop()
        helper(1, [], 0)
        return ans
