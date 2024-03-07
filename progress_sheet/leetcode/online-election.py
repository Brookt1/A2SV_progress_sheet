class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.persons = persons
        self.times = times
        self.dic = Counter()
        self.winner = []
        
        _max = [0,0]

        for person in persons:
            self.dic[person] += 1
            if _max[0] <= self.dic[person]:
                _max = [self.dic[person], person]
            self.winner.append(_max[1])

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t)
        return self.winner[idx - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)