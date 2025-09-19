from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo_result = {}

        def recurse(L, R):
            if (L, R) in memo_result:
                return memo_result[(L, R)]
            if R - L < 2:
                return 0  # Too close together
            if R - L == 2:
                result = nums[L] * nums[R] * nums[L + 1]
                memo_result[(L, R)] = result
                # print(f"Max between {nums[L]} and {nums[R]} is {memo_result[L,R]}")
                return memo_result[(L, R)]
            local_result = -800000000000000
            for i in range(L + 1, R):
                local_result = max(
                    [
                        local_result,
                        nums[L] * nums[R] * nums[i] + recurse(L, i) + recurse(i, R),
                    ]
                )
            memo_result[(L, R)] = local_result
            # print(f"Max between {nums[L]} and {nums[R]} is {memo_result[L,R]}")
            return memo_result[(L, R)]

        return recurse(0, len(nums) - 1)


print(Solution().maxCoins([3, 1, 5, 8]))
print(Solution().maxCoins([1, 5]))
print(Solution().maxCoins([5]))
