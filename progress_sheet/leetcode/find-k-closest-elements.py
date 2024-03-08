class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ans = []
        for i in range(k):

            left, right = 0, len(arr) -1 
            diff = left + (right - left)//2 
            while left <= right:

                mid = left + (right - left)//2
                if abs(arr[mid] - x) < abs(arr[diff] - x):
                    diff = mid
                elif abs(arr[mid] - x) == abs(arr[diff] - x) and diff > mid:
                    diff = mid

                if arr[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
            
            ans.append(arr[diff])
            arr = arr[:diff] + arr[diff + 1: ]
        ans.sort()
        return ans

