class Solution:
    def minOperations(self, logs: List[str]) -> int:


        stack=[]

        for ch in logs:

            if ch=='../' :
                if stack:
                    stack.pop()
            elif ch=='./':
                pass
            else:
                stack.append(ch)
        return len(stack)
        