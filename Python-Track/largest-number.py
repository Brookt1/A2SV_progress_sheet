class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=sorted(nums,key=cmp_to_key(self.compare),reverse=True)
        if res[0]==0:
            return str(0)
        return ''.join(str(x) for x in res)

    def compare(self, a: int,b: int)->int:
        if int(str(a)+str(b))>=int(str(b)+str(a)):
            return 1
        return -1