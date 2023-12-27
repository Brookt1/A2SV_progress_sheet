class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:


        even_sum=sum(num for num in nums if num%2==0)
        res=[]
        for val, idx in queries:
            if nums[idx]%2==0: 
                if (nums[idx]+val)%2==0:
                    even_sum+=val
                else:
                    even_sum-=nums[idx]
            else:
                if (nums[idx]+val)%2==0:
                    even_sum+=(nums[idx]+val)
            
            res.append(even_sum)
            nums[idx]+=val
        return res
        

        
        