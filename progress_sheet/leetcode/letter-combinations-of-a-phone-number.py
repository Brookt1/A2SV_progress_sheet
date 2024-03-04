class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        map = {'2':'abc','3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        

        ans = []
        def helper(idx, path):
            if idx == len(digits):
                if path:
                    ans.append(''.join(path.copy()))
                return

            for ch in map[digits[idx]]:

                path.append(ch)
                helper(idx + 1, path)
                path.pop()
        helper(0, [])
        return ans