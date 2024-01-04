class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res=[]

        i=len(digits)-1
        while i<len(digits):
            if digits[i]==9:
                digits[i]=0
            else:
                break
            i-=1
        if i<0:
            return [1] + digits

        else:
            digits[i]+=1
            return digits
