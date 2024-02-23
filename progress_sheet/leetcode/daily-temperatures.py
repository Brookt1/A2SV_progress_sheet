class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[]
        ans=[]
        for i in range(len(temperatures)-1,-1,-1):

            count=1
            while stack and stack[-1][0]<=temperatures[i]:
                count+=stack[-1][1]
                stack.pop()
            if stack:
                ans.append(count)
            else:
                ans.append(0)
            stack.append([temperatures[i],count])

        return reversed(ans)
