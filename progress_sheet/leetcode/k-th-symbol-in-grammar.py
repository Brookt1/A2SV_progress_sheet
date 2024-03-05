class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recu(n, k):
            if n == 0:
                return 0
            val = recu(n-1, ceil(k/2))
            is_k_odd = k % 2 == 1
            if val:
                return 1 if is_k_odd else 0
            else:
                return 0 if is_k_odd else 1
        return recu(n,k)

