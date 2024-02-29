class Solution:
    def numberOfWays(self, s: str) -> int:


        prefix = [0]

        for ch in s:
            if ch == '0':
                prefix.append(prefix[-1])
            else:
                prefix.append(prefix[-1] + 1)
        
        res = 0
        for i in range(1,len(prefix)):
            num_one = prefix[-1] - prefix[i]
            if s[i-1] == '0':
                res += (prefix[i-1]) * (num_one)
            else:
                res += (i - prefix[i]) * (len(s)-i - num_one)
                
        return res

        