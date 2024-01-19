class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n=len(nums)
        visted=set()
        for left in range(n):

            if left not in visted:
                last=right=left
                local=set()
                while nums[right]*nums[left]>0:

                    if right in local:
                        if  right!=last:
                            return True
                        break
                    visted.add(right)
                    local.add(right)
                    last=right
                    right=(right+nums[right])%n
        return False
        