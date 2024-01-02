class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        left,right=0,sum(nums)
        res,max_val=[],right
        for idx,val in enumerate(nums):

            if left+right==max_val:
                res.append(idx)
            elif left+right>max_val:
                max_val=left+right
                res=[idx]
            if val==0:
                left+=1
            else:
                right-=1
        
        if left+right==max_val:
            res.append(len(nums))
        elif left+right>max_val:
            res=[len(nums)]
        return res   