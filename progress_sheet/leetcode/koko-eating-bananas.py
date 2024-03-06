class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        


        low, high = 1, max(piles)
        while low <= high:
            mid = low + (high - low)//2
            count_hour = 0
            for i in range(len(piles)):
                count_hour += ceil(piles[i]/mid)
            if count_hour > h:
                low = mid + 1
            else:
                high = mid - 1
        return low