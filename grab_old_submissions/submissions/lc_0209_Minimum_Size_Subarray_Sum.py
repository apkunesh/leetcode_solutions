class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                cur_len = right-left+1 # May not need this
                min_len = min(cur_len,min_len)
                cur_sum -= nums[left]
                left+=1
        return 0 if min_len == float("inf") else min_len