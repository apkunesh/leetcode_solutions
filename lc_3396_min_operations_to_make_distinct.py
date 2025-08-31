from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Idea: move from right-to-left, keeping track of the #s we've seen so far in a set. As soon as we see one we've already seen, we must stop. We can then easily compute the # to ensure we trim that index.
        num_set = set()
        dupe_index = None
        for num_ind in range(len(nums) - 1, -1, -1):
            if nums[num_ind] not in num_set:
                num_set.add(nums[num_ind])
            else:
                dupe_index = num_ind
                break
        if dupe_index is None:
            return 0
        return dupe_index // 3 + 1
