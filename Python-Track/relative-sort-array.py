class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        counter=Counter(arr1)
        res=[]
        for num in arr2:
            res=res+[num]*counter[num]
            del counter[num]
        temp=[]
        for key,val in counter.items():
            for i in range(val):
                temp.append(key)
        return res + sorted(temp)

        