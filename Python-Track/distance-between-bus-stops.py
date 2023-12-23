class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        dis=sum(distance[start:destination]) if start<destination else sum(distance[start:]+distance[:destination])

        return min(sum(distance)-dis,dis)
        