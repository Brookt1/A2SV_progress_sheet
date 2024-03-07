class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        res = []
        for idx, a in enumerate(costs):
            res.append([abs(a[1] - a[0]), idx])
        res.sort(reverse=True)

        count_a = 0
        count_b = 0

        cost = 0
        for i in range(len(costs)):
            cost_a, cost_b = costs[res[i][1]]
            if count_a == n//2:
                cost +=cost_b
            elif count_b == n//2:
                cost +=cost_a
            else:
                if cost_a < cost_b:
                    count_a +=1
                    cost += cost_a
                else:
                    count_b +=1
                    cost +=cost_b

        return cost