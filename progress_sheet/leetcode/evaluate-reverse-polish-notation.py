class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        oper={'+','-','*','/'}
        for token in tokens:
            if token in oper:
                val=str(int(eval(stack[-2] + token +stack[-1])))
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(token)
        return int(stack[0])


        