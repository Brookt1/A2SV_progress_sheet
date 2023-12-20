class Solution:
    def average(self, salary: List[int]) -> float:

        sum,i=0,1
        salary.sort()
        while i<len(salary)-1:
            sum+=salary[i]
            i+=1
        return sum/(i-1)
        