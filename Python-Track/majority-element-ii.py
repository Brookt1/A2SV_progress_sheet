class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cou=Counter(nums)
        res,n=[],len(nums)//3
        for key, val in cou.items():
            if val>n: res.append(key)
        return res

        