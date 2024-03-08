class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0]
        for ch in customers:
            if ch == 'N':
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        
        cost = [math.inf, -1]
        for i in range(1, len(prefix)):
            c = prefix[i - 1] +  len(prefix) - i - (prefix[-1] - prefix[i - 1])
            if  c < cost[0]:
                cost = [c, i]
        if cost[0] > prefix[ -1]:
            return len(customers)
        
        return cost[1] - 1



        