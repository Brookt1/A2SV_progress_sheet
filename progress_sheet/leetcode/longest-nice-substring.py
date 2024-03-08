class Solution:
    def longestNiceSubstring(self, s: str) -> str:



        def helper(s):
            if s is None:
                return ''
            
            dic = set(s)
            idx = -1
            for i in range(len(s)):
                if s[i].lower() not in dic or s[i].upper() not in dic :
                    idx = i
                    break
            if idx < 0:
                return s
            
            left = helper(s[ : idx])
            right = helper(s[idx + 1:])

            if len(right) > len(left):
                return right
            return left
        return helper(s)


        