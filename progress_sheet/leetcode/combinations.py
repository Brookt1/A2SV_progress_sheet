class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def comb(i,n, k, cur_comb):
            if len(cur_comb) == k:
                self.ans.append(cur_comb.copy())
            if i> n: return
            for j in range(i, n+1):
                cur_comb.append(j)
                comb(j+1, n, k, cur_comb)
                cur_comb.pop()
            
        comb(1, n, k, [])
        return self.ans