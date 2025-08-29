class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps,old_horizon,horizon = 1,0,nums[0]+1
        while horizon < len(nums):
            new_horizon = horizon
            for i in range(old_horizon,horizon):
                new_horizon = max(i+nums[i]+1,new_horizon)
            jumps+=1
            old_horizon = horizon
            horizon = new_horizon
        return jumps