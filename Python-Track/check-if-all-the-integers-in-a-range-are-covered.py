class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        hs=set()
        for s,e in ranges:
            for i in range(s,e+1):
                hs.add(i)
        print(hs)
        for i in range(left,right+1):
            if i not in hs: return False

        return True
        