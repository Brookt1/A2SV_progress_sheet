class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    
        
        nums.sort()
        left, right = 1, nums[-1]
        while left <= right:
            mid = left + (right -left)//2
            div_sum = 0
            for num in nums:
                div_sum +=ceil(num/mid)
            if div_sum > threshold:

                left = mid + 1
            else:
                right = mid - 1

        return left
        