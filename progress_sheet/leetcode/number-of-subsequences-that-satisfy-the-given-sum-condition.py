class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        mod = int(1e9 + 7)

        nums.sort()
        ans = 0
        for i in range(len(nums)):
            left, right = i, len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] + nums[i] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if right >= i:
                ans += (pow(2, right - i)) % mod
        return ans % mod

            