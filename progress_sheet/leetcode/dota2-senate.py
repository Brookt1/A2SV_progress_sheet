class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        deq=deque(senate)
        count=Counter(senate)
        denounce=0
        while count['R'] and count['D']:
            ch = deq.popleft()

            if denounce==0:
                denounce += 1
                deq.append(ch)
            elif ch == deq[-1]:
                deq.append(ch)
                denounce += 1
            else:
                denounce-=1
                count[ch]-=1

        if count['R']:
            return 'Radiant'
        return 'Dire'