class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        left,num_white=0,0
        res=k+1
        for right in range(len(blocks)):
            if blocks[right]=='W':
                num_white+=1
            if right-left+1==k:
                res=min(res,num_white)
                if blocks[left]=='W':
                    num_white-=1
                left+=1
        return res

         
        