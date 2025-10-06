from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Idea: scan across nums and recover: (1) the max subarray sum (kadane), (2) the min subarray sum (kadane, most negative), (3) the grand max
        # The result is then *either* the grand max minus the min subarray sum OR the max subarray sum.
        cur_max, cur_min, grand_max, grand_min, grand_total = [
            0,
            0,
            -10 * 10**30,
            10 * 10**30,
            0,
        ]
        for i in range(len(nums)):
            cur_max = cur_max + nums[i]
            grand_max = max([grand_max, cur_max])
            # print(f"Grand max has become {grand_max} after checking element {nums[i]}")
            cur_min = cur_min + nums[i]
            grand_min = min([grand_min, cur_min])
            if cur_max < 0:
                cur_max = 0
            if cur_min > 0:
                cur_min = 0
            grand_total += nums[i]
        minimum_result = grand_total - grand_min
        # print(f"Minimum Result {minimum_result}, Positive Result {grand_max}")
        if minimum_result == 0:
            minimum_result = -3 * 10**30
        return max([grand_max, minimum_result])


print(f"{Solution().maxSubarraySumCircular([1,-2,3,-2])} should be 3")
print(f"{Solution().maxSubarraySumCircular([5,-3,5])} should be 10")
print(f"{Solution().maxSubarraySumCircular([-3,-2,-3])} should be -2")


"""
Input: nums = [1,-2,3,-2]
Output: 3


Input: nums = [5,-3,5]
Output: 10


Input: nums = [-3,-2,-3]
Output: -2
"""
