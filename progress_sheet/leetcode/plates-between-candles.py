class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)
        ans = []
        for left, right in queries:
            l = bisect.bisect_left(candles, left)
            r = bisect.bisect_right(candles, right) - 1
            # print(l, r)
            if l >= r:
                ans.append(0)
            else:
                leng = candles[r] - candles[l] + 1
                leng -= r - l + 1
                ans.append(leng)
            # print(ans)
        return ans
