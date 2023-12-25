class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        win={}
        loser={}
        for w, l in matches:

            win[w]=win[w] + 1 if w in win else 1
            loser[l]=loser[l]+1 if l in loser else 1
        res=[[],[]]
        print(loser)
        for w in win:
            if w not in loser:res[0].append(w)
        for k,l in loser.items():
            if l==1: res[1].append(k)
        res[0].sort()
        res[1].sort()
        return res
        