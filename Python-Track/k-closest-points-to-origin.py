class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis=[]
        for x,y in points:
            sqr=x**2+y**2
            dis.append([sqr,[x,y]])

        dis.sort()
        print(dis)
        res=[]
        for i in range(k):
            res.append(dis[i][1])
        return res

        