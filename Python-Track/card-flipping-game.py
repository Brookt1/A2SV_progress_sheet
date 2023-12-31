class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        bothSide=set()
        ans=2001
        for i in range(len(fronts)):
            if fronts[i]==backs[i]: bothSide.add(fronts[i])
        for i in range(len(fronts)):
            if fronts[i] not in bothSide:
                ans=min(ans,fronts[i])
            if backs[i] not in bothSide:
                ans=min(ans,backs[i])
        return ans if ans!=2001 else 0

