class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        max_val = max(citations)
        ans = 0
        for num in range(1, max_val + 1):
            left,right=0, len(citations) - 1
            while left <= right:
                mid = left + (right - left)//2
                if citations[mid] >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            if left >= len(citations) or len(citations) - left < num:
                break

            ans = num     

        return ans