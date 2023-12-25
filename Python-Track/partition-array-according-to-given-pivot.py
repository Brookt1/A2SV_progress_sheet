class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less=[]
        more=[]

        for num in nums:
            if num<pivot: less.append(num)
            elif num>pivot: more.append(num)
        res=[]
        res.extend(less)
        print(less)
        for i in range(len(nums)-(len(less)+len(more))): res.append(pivot)
        res.extend(more)

        return res
        