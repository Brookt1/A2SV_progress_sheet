class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # if letters[-1] < target:
        #     return letters[0]

        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left)//2
            print(left, right)
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left < len(letters):
            return letters[left]
        return letters[0]