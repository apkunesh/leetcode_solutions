class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        d=0
        for i in range(len(nums)-2,-1,-1):
            d+=1
            if nums[i] >= d:
                if i == 0:
                    return True
                d=0
        return False