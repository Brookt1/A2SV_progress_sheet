class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:



        stack = []
        copy = nums + nums
        stored ={}
        for num in copy:
            while stack and stack[-1] < num:
                n = stack.pop()
                if n in stored:
                    stored[n].append(num)
                else:
                    stored[n] = [num]
            stack.append(num)
        index = Counter()
        ans = []
        for num in nums:
            if num in stored:
                ans.append(stored[num][index[num]])
                index[num] +=1
            else:
                ans.append(-1)
        return ans

        