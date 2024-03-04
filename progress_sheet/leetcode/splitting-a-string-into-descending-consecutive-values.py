class Solution:
    def splitString(self, s: str) -> bool:



        def backtrack(index, path):
            if index == len(s):
                if len(path)>1:
                    return True
                return False
            

            for i in range(index, len(s)):
                sub_string = int(s[index: i+1])
                if not path or path[-1] - sub_string == 1:
                    path.append(sub_string)
                    if backtrack(i+1, path):
                        return True
                    path.pop()
                    
            
            res = backtrack(index+1, [int(s[:index + 1])])
            return res

        ans = backtrack(0, [])
        print(ans)
        return ans


                    
