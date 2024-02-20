class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        



        left,minEnd=0,float('inf')
        shoot=0
        points.sort()
        for right in range(len(points)):

            if minEnd<points[right][0]:
                shoot+=1
                minEnd=points[right][1]
            else:
                minEnd=min(minEnd,points[right][1])
        return shoot+1


