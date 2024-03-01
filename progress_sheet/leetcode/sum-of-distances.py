class Solution:
    def distance(self, nums: List[int]) -> List[int]:


        dic = {}

        for idx, num in enumerate(nums):

            if num in dic:
                dic[num].append(dic[num][-1] + idx)
            else:
                dic[num] = [0,idx]
        ans = []
        idx_holder = Counter()
        for idx, num in enumerate(nums):
            prefix = dic[num]
            pre_idx = idx_holder[num]+1


            left = abs(prefix[pre_idx-1] - idx * (pre_idx-1))
            right = prefix[-1] - prefix[pre_idx] - idx * (len(prefix) - pre_idx -1)
            ans.append(left + right)

            idx_holder[num] +=1
        return ans
        