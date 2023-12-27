class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        
        ans=[]
        for idx in range(len(boxes)):
            sum=0
            for  i in range(len(boxes)):
               if i == idx: continue
               if boxes[i]=='1': sum+=abs(i-idx)
            ans.append(sum)
        return ans