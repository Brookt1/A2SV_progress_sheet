class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        tot_time=0
        for i in range(len(points)-1):

            tot_time+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
        return tot_time
        