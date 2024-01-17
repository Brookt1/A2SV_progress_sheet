class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel=('a','e','i','o','u')
        left,res=0,0
        num_vowel=0
        for right in range(len(s)):
            if s[right] in vowel:
                num_vowel+=1
            if right-left+1==k:
                res=max(res,num_vowel)
                if s[left] in vowel:
                    num_vowel-=1
                left+=1
        return res
    