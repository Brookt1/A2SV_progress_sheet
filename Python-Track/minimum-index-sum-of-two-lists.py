class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        idx=len(list1)+len(list2)
        res=[]
        for i,val in enumerate(list1):
            n=list2.index(val) if val in list2 else -1
            if n>-1 and n+i<=idx: 
                if n+i==idx:
                    res.append(val)
                else: 
                    res=[val]
                    idx=n+i
        return res