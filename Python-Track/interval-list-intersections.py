class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:




        first,second=0,0
        res=[]
        while first<len(firstList) and second<len(secondList):

            firstSta,firstEnd=firstList[first]
            secondSta,secondEnd=secondList[second]
            if firstEnd>=secondSta and secondEnd>=firstSta:
                res.append([max(secondSta,firstSta) , min(firstEnd,secondEnd)])
            
            if firstEnd>secondEnd:
                second+=1
            elif secondEnd>firstEnd:
                first+=1
            else:
                first+=1
                second+=1
        return res




        