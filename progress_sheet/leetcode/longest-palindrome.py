class Solution:
    def longestPalindrome(self, s: str) -> int:

        count=Counter(s)
        ans=0
        for key, val in count.items():
            if val%2!=0:

                ans+=val-1
                if val>1:
                    count[key]=1
            else:
                ans+=val
                count[key]=0
        if sum(count.values())>0:
            ans+=1
        return ans

        