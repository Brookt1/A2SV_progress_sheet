class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(path, pare_diff):
            if len(path) == n*2:
                ans.append(''.join(path))
                return
        
            if pare_diff == 0:
                path.append('(')
                helper(path, pare_diff + 1)
                path.pop()
                
            elif len(path) + pare_diff == n*2:
                path.append(')')
                helper(path, pare_diff - 1)
                path.pop()
            else:
                path.append('(')
                helper(path, pare_diff + 1)

                path.pop()

                path.append(')')
                helper(path, pare_diff - 1)

                path.pop()
        helper([], 0)
        return ans




