class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cou=Counter(arr)
        return sorted(list(cou.items()),key=lambda x: x[1])[-1][0]
        