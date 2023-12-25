class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg,pos=[],[]
        for num in nums:
            if num<0: neg.append(num)
            else: pos.append(num)
        res=[]
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])
        return res