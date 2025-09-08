# NOTE: This one was not completed. I believe the solution should look like:
#      1) Do DP where the table contains score, hashset from index to node, and linkedlist of nodes representing balloons
#      2) Rows represent # of element popped, columns represent allowed choices.
#      3) For a given position in the table, we need to consider 3 possibilities for the "best":
#           3a) The one to our left. Essentially, "adding the new element doesn't affect which we should choose so far."
#           3b) The one to our top-left. "The best without access to the current element." If we add in our new element, we can compare.
#           3c) The one directly above: "The best with the same # of options but fewer choices."
#               3ci) If this is the same as 3b, ... Brain is dead, have to return to this later.

# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100

"""
Nums array, size n. burst i, get nums[i-1]*nums[i]*nums[i+1] coins. OOB has a value of 1.
Return max # of coins you can receive by bursting all balloons.
COOL!

Almost certainly 2d dynamic programming problem.
I notice that I can construct the same result by *inserting* values. Not sure I wanna do that but let's look.

Notice also that in the example, we always pop the smallest first. Is there an obvious counterexample?

"""


from typing import Dict, List, Optional, Set


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cached_values = {}

        def max_given_balloon_set(
            balloon_set: Set[int],
            index_to_left: Dict[int, Optional[int]],
            index_to_right: Dict[int, Optional[int]],
            leftmost: Optional[int] = None,
        ) -> int:
            if len(balloon_set) == 0:
                return 0
            cur = leftmost
            key_list = [cur]
            while cur:
                key_list.append(index_to_right[cur])
            cache_key = tuple(key_list)
            if (
                cache_key in cached_values
            ):  # TODO: Perhaps reconstruct this in order if tupling isn't enough
                return cached_values[cache_key]
            indices_to_check, score_list = list(balloon_set), []
            for i in range(len(indices_to_check)):
                elem = indices_to_check[i]
                old_elem_left, old_elem_right = index_to_left.get(
                    elem
                ), index_to_right.get(elem)
                pop_value = (
                    nums[elem]
                    * (nums[old_elem_left] if old_elem_left is not None else 1)
                    * (nums[old_elem_right] if old_elem_right is not None else 1)
                )
                if elem == leftmost:
                    leftmost = index_to_right[elem]
                if old_elem_left is not None:
                    index_to_right[old_elem_left] = index_to_right[elem]
                if old_elem_right is not None:
                    index_to_left[old_elem_right] = index_to_left[elem]
                balloon_set.remove(elem)
                max_future = max_given_balloon_set(
                    balloon_set, index_to_left, index_to_right, leftmost
                )
                balloon_set.add(elem)
                if old_elem_right is not None:
                    index_to_left[old_elem_right] = elem
                if old_elem_left is not None:
                    index_to_right[old_elem_left] = elem
                score_list.append(max_future + pop_value)
            cached_values[cache_key] = max(score_list)
            return cached_values[cache_key]

        balloon_set = set(range(len(nums)))
        i_to_l: Dict[int, Optional[int]] = {0: None}
        i_to_r: Dict[int, Optional[int]] = {len(nums) - 1: None}
        if len(nums) > 1:
            i_to_l[len(nums) - 1] = len(nums) - 2
            i_to_r[0] = 1
        for i in range(1, len(nums) - 1):
            i_to_l[i], i_to_r[i] = i - 1, i + 1
        grand_max = max_given_balloon_set(
            balloon_set=balloon_set,
            index_to_left=i_to_l,
            index_to_right=i_to_r,
            leftmost=0,
        )
        return grand_max
