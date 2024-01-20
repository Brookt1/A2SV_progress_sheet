class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        res=[]
        for i in range(len(arr)-1,-1,-1):
            for j in range(i+1):
                if arr[j]==i+1:
                    break
            arr=list(reversed(arr[:j+1]))+arr[j+1:]
            arr=list(reversed(arr[:i+1]))+arr[i+1:]
            res.append(j+1)
            res.append(i+1)
        return res
        