class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        

        def helper(arr,p):

            if len(arr) == 0:

                return [0, 0]
            
            left=helper(arr[1:],2 if p==1 else 1)
            right=helper(arr[:len(arr)-1],2 if p==1 else 1)

            if p == 1:
                left[0] += arr[0]
                right[0] += arr[-1]
                if left[0] < right[0]:
                    return right
                else:
                    return left
        
            else:
                left[1] += arr[0]
                right[1] += arr[-1]
                if left[1]<right[1]:
                    return right
                else:
                    return left
        ans = helper(nums, 1)
        return ans[0] >= ans[1]
        