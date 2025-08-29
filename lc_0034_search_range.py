from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        L, R = 0, len(nums) - 1
        candidate_ind = (L + R) // 2
        # Try find left first
        while L < R:
            if nums[candidate_ind] >= target:
                R = candidate_ind
            else:
                L = candidate_ind + 1
            candidate_ind = (L + R) // 2
        minimum_ind = candidate_ind if nums[candidate_ind] == target else -1
        L, R = 0, len(nums) - 1
        candidate_ind = (L + R + 1) // 2
        while L < R:
            if nums[candidate_ind] <= target:
                L = candidate_ind
            else:
                R = candidate_ind - 1
            candidate_ind = (L + R + 1) // 2
        maximum_ind = candidate_ind if nums[candidate_ind] == target else -1
        return [minimum_ind, maximum_ind]
