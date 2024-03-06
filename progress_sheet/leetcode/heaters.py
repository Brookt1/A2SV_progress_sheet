class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        

        heaters.sort()
        ans = 0
        for house in houses:

            left, right, best = 0, len(heaters) - 1, math.inf
            while left <= right:
                mid = left + (right - left)//2
                best = min(abs(house- heaters[mid]), best)
                if heaters[mid] >  house:
                    right = mid - 1
                elif heaters[mid] < house:
                    left = mid + 1
                else:
                    break
            ans = max(ans, best)
        return ans