class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x=num//3
        if num%3==0: return [x-1,x,x+1]
        else: return []