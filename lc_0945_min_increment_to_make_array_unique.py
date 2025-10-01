from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Simple construct would be O(n**2). Instead we want to figure out *where to place outside known boundary* -> just place it there.
        # This would then become basically just binary search.
        # So equivalent would be to sort (nlogn)
        if len(nums) <= 1:
            return 0
        nums.sort()
        grand_result = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                grand_result += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return grand_result


print(Solution().minIncrementForUnique([1, 2, 2]))  # 1
print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))  # 6
print(Solution().minIncrementForUnique([0, 2, 2]))  # 1
print(Solution().minIncrementForUnique([7, 2, 7, 2, 1, 4, 3, 1, 4, 8]))  # 16

print(
    Solution().minIncrementForUnique(
        [14, 4, 5, 14, 13, 14, 10, 17, 2, 12, 2, 14, 7, 13, 14, 13, 4, 16, 4, 10]
    )
)  # 41

# Input: nums = [1,2,2]
# Output: 1
#
#
# Input: nums = [3,2,1,2,1,7]
# Output: 6
