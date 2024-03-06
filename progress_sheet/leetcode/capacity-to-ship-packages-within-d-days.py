class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:



        left, right = max(weights), sum(weights)

        while left <= right:

            mid = left +  (right - left)//2
            count_day = 1
            weight_sum = 0
            for i in range(len(weights)):
                weight_sum += weights[i]
                if weight_sum > mid:
                    count_day += 1
                    weight_sum = weights[i]
            if count_day <= days:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
                
