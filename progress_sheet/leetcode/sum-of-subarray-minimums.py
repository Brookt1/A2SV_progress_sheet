class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
    
        stack=[]
        res=0
        for i in range(len(arr)):
            while stack and stack[-1][1]>arr[i]:
                temp=stack.pop()
                left=-1 if not stack else stack[-1][0]
                res+=(temp[0]-left)*(i-temp[0])*temp[1]
            stack.append([i,arr[i]])
        
        for i in range(len(stack)):
            left=-1 if i==0 else stack[i-1][0]
            res+=(stack[i][0]-left)*(len(arr)-stack[i][0])*stack[i][1]
        return res%(10**9+7)