class Solution:
    def scoreOfParentheses(self, s: str) -> int:


        stack=[]
        curr_sum=0
        for ch in s:
            if ch=='(':
                stack.append(curr_sum)
            else:
                diff=curr_sum-stack.pop()
                
                if diff>0:
                    curr_sum-=diff
                    curr_sum+=(diff*2)
                else:
                    curr_sum+=1
        return curr_sum