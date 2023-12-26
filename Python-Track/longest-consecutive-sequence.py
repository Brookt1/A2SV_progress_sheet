class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for i in numSet:
            
            if i-1 not in numSet:
                l=1
                while l+i in numSet:
                    l+=1
                longest=max(longest,l)
        return longest

