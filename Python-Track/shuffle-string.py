class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[1 for _ in range(len(s))]
        for idx,val in enumerate(s):
            res[indices[idx]]=val
        return ''.join(res)
