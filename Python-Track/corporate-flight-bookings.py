class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        booked=[0]*n
        for first,last,seat in bookings:
            booked[first-1]+=seat
            if last<n:
                booked[last]-=seat
        for i in range(1,n):
            booked[i]+=booked[i-1]
        return booked

        