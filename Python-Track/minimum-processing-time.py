class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        

        processorTime.sort(reverse=True)
        tasks.sort()
        n=len(tasks)//len(processorTime)
        res=0
        idx=0
        for i in range(n-1,len(tasks),n):
            res=max(res,processorTime[idx]+tasks[i])
            idx+=1
        return res



