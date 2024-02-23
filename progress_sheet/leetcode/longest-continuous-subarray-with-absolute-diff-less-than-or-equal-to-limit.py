class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:


        left=ans=0

        min_que=deque()
        max_que=deque()
        for right in range(len(nums)):

            while min_que and min_que[-1]>nums[right]:
                min_que.pop()
            min_que.append(nums[right])
            while max_que and max_que[-1]<nums[right]:
                max_que.pop()
            max_que.append(nums[right])

            while max_que[0]-min_que[0]>limit:
                if nums[left]==min_que[0]:
                    min_que.popleft()
                if nums[left]==max_que[0]:
                    max_que.popleft()
                left+=1
            ans=max(ans,right-left+1)
        return ans




        