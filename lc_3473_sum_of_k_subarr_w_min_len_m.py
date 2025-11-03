from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        """
        Been turning this one over in my head for a while. Here's what I think we need to do:
         - Compute the prefix sum array
         - Use the prefix sum array to create the following:
            - A map from a start, end index range + n windows to the best sum from that range
        """
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        cache = {}
        print(f"PREFIX SUM {prefix_sum}")

        def recurse(start, end, windows):
            if end - start < m or start > len(nums) - m - 1 or end >= len(nums):
                print("returning")
                return -(10**10)
            if windows == 1:
                not_included = recurse(start + 1, end, 1)
                starts_with = (
                    prefix_sum[start + m - 1] - prefix_sum[start - 1]
                    if start - 1 > 0
                    else prefix_sum[start + m - 1]
                )
                if (start, end) == (2, 3):
                    print(starts_with)
                for i in range(start + m, end + 1):
                    starts_with = max(
                        starts_with,
                        (
                            prefix_sum[i] - prefix_sum[start - 1]
                            if start - 1 > 0
                            else prefix_sum[i]
                        ),
                    )
                cache[(start, end, windows)] = max(starts_with, not_included)
            else:
                last_end = len(nums) - ((windows - 1) * m) + 1
                print(f"Last end will be {last_end}")
                grand_max = -(10**10)
                for part in range(start + m, last_end):
                    right_part = recurse(part, len(nums) - 1, windows - 1)
                    left_part = recurse(start, part, 1)
                    grand_max = max(grand_max, left_part + right_part)
                cache[(start, end, windows)] = grand_max
            return cache[(start, end, windows)]

        result = recurse(0, len(nums) - 1, k)
        print(cache)
        return result


print(Solution().maxSum([-10, 3, -1, -2], 4, 1))
