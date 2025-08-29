class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = floor((right+left)/2)
            middle_val = nums[middle]
            if middle_val > target:
                right = middle - 1
            elif middle_val < target:
                left = middle + 1
            else:
                return middle
        return -1
