from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        z = 0
        while z < len(nums) and nums[z] != 0:
            z += 1
        r = z
        while r < len(nums):
            while r < len(nums) and nums[r] == 0:
                r += 1
            if r == len(nums):
                return nums
            nums[z] = nums[r]
            nums[r] = 0
            while z < len(nums) and nums[z] != 0:
                z += 1
            if z == len(nums):
                return nums
            r += 1
        return nums


soln = Solution().applyOperations
print(soln([1, 2, 2, 1, 1, 0]))  # [1,4,2,0,0,0]
print(soln([1, 0]))  # [1,0]
