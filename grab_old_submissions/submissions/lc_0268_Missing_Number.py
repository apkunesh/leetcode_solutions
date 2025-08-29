class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        running_total = 0
        for i in range(len(nums)):
            running_total += (i+1) - nums[i]
        return running_total