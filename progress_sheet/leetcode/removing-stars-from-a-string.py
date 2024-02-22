class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for w in s:
            if w == "*":
                stack.pop()
            else:
                stack.append(w)
        return "".join(stack)
        