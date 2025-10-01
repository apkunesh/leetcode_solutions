from typing import List, Optional


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Idea: given an index, and p, find minimal max to right.
        # Then at top level, we just do this on 0 with the actual p.
        if p == 0:
            return 0
        min_cost_cache = {}
        nums.sort()
        print("Sorted list is ", nums)

        def recurse(i, p) -> Optional[int]:
            if (i, p) in min_cost_cache:
                print(f"{[i,p]} cache hit, {min_cost_cache[(i,p)]}")
                return min_cost_cache[(i, p)]
            if i >= len(nums) - 1:
                print(f"Beyond nums at index {i}")
                return None
            elements = len(nums) - i
            if elements < 2 * p:
                print(
                    f"Index {i} does not have enough following elements -- need >= {2*p}"
                )
                return None
            if p == 1:
                local_min = 10**35
                for l in range(i, len(nums) - 1):
                    local_min = min(local_min, nums[l + 1] - nums[l])
                    print("New local min: ", local_min)
                min_cost_cache[(i, p)] = local_min
                return min_cost_cache[(i, p)]
            else:
                local_min = 10**35
                for j in range(i, len(nums) - 1):
                    # Assume we include the current one, plus the best to the right
                    print("Recursing from ", j)
                    print("")
                    right_result = recurse(j + 2, p - 1)
                    if right_result is None:
                        break
                    print(f"min to right of {j+1} is ", right_result)
                    local_min = min(local_min, nums[j + 1] - nums[j] + right_result)
                if local_min == 10**35:
                    min_cost_cache[(i, p)] = None
                    return min_cost_cache[(i, p)]
                min_cost_cache[(i, p)] = local_min
                return min_cost_cache[(i, p)]

        grand_result = recurse(0, p)
        if grand_result is None:
            return -1
        print(min_cost_cache)
        return grand_result


# r1 = Solution().minimizeMax([10, 1, 2, 7, 1, 3], 2)
# assert r1 == 1, r1
#
# r2 = Solution().minimizeMax([4, 2, 1, 2], 1)
# assert r2 == 0, r2
#
r3 = Solution().minimizeMax([8, 9, 1, 5, 4, 3, 6, 4, 3, 7], 4)
print(r3)

# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
#
#
# Input: nums = [4,2,1,2], p = 1
# Output: 0
