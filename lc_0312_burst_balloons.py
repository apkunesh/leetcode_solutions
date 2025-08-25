# NOTE: This one was not completed. I believe the solution should look like:
#      1) Do DP where the table contains score, hashset from index to node, and linkedlist of nodes representing balloons
#      2) Rows represent # of element popped, columns represent allowed choices.
#      3) For a given position in the table, we need to consider 3 possibilities for the "best":
#           3a) The one to our left. Essentially, "adding the new element doesn't affect which we should choose so far."
#           3b) The one to our top-left. "The best without access to the current element." If we add in our new element, we can compare.
#           3c) The one directly above: "The best with the same # of options but fewer choices."
#               3ci) If this is the same as 3b, ... Brain is dead, have to return to this later.

"""
Nums array, size n. burst i, get nums[i-1]*nums[i]*nums[i+1] coins. OOB has a value of 1.
Return max # of coins you can receive by bursting all balloons.
COOL!

Almost certainly 2d dynamic programming problem.
I notice that I can construct the same result by *inserting* values. Not sure I wanna do that but let's look.

Notice also that in the example, we always pop the smallest first. Is there an obvious counterexample?

"""


from typing import Dict, List, Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None


# Let's do brute force and improve on it
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        l_dum = Node(1)
        r_dum = Node(1)
        l_dum.right = r_dum
        r_dum.left = l_dum
        cur_left = l_dum
        index_to_node = {}
        for i in range(len(nums)):
            cur_left.right = Node(nums[i])
            r_dum.left = cur_left.right
            cur_left.right.left = cur_left
            cur_left.right.right = r_dum
            index_to_node[i] = cur_left.right
            cur_left = cur_left.right

        grand_max = {"val": 0}

        def recurse(i: int, index_to_node: Dict[int, Node], total: int):
            if len(index_to_node) == 1:
                difference = index_to_node[i].val
                total = total + difference
                grand_max["val"] = max(total, grand_max["val"])
                total -= difference
                return
            happy_node = index_to_node.pop(i)
            difference = happy_node.val * happy_node.left.val * happy_node.right.val  # type: ignore
            this_level_left = happy_node.left
            this_level_right = happy_node.right
            this_level_left.right = this_level_right
            this_level_right.left = this_level_left
            total = total + difference
            keys_here = list(index_to_node.keys())
            for index in keys_here:
                recurse(index, index_to_node, total)
            index_to_node[i] = happy_node
            this_level_left.right = happy_node
            this_level_right.left = happy_node

        for i in range(len(nums)):
            recurse(i, index_to_node, 0)
        return grand_max["val"]
