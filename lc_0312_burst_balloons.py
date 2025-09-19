from collections import deque
from typing import Dict, List, Tuple


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        General idea:
         - Start assuming 0 balloons
         - What would score be if each of the numbs was the final balloon popped?
         - Now we can add in the next balloon
         - For each balloon combination, there's an associated max. Store this max in memory. We can discard each previous (now-unneeded) layer.
         Notice that doing it this way (with inserts) is, like, O(n) every time, since we're adding in at specific indices. It'd be nice to avoid this.
         LinkedLists would simplify the *process* of figuring out who my neighbors are, but it's not exactly ideal...
         OH! I can think of it as adding in values *between* elements that are already present.
        """

        def construct_new_ordered_num(numset, new_index):
            candidate = numset[0]
            result = []
            i = 0
            while candidate[0] < new_index:
                result.append(candidate)
                i += 1
                candidate = numset[i]
            result.append((new_index, nums[new_index]))
            while i < len(numset):
                candidate = numset[i]
                result.append(candidate)
                i += 1
            return result

        ordered_nums = deque([[(-1, 1), (len(nums), 1)]])
        score_map: Dict[Tuple, int] = {(-1, len(nums)): 0}
        count = 0
        while ordered_nums:
            # print("")
            # print(f"ROUND {count}")
            for _ in range(len(ordered_nums)):
                numset = ordered_nums.popleft()
                old_tuple = tuple([elem[0] for elem in numset])
                for left_part, right_part in zip(numset[:-1], numset[1:]):
                    index_tuple = (left_part[0], right_part[0])
                    for i in range(index_tuple[0] + 1, index_tuple[1]):
                        local_score = (
                            left_part[1] * nums[i] * right_part[1]
                            + score_map[old_tuple]
                        )
                        new_ordered_num = construct_new_ordered_num(numset, i)
                        new_tuple = tuple([elem[0] for elem in new_ordered_num])
                        if score_map.get(new_tuple) is None:
                            score_map[new_tuple] = local_score
                            # print(f"New tuple: {new_tuple}")
                            ordered_nums.append(new_ordered_num)
                        else:
                            score_map[new_tuple] = max(
                                [score_map[new_tuple], local_score]
                            )
            count += 1
        return score_map[tuple([i for i in range(-1, len(nums) + 1)])]


ex1 = Solution().maxCoins([3, 1, 5, 8])
print(f"{ex1==167}, result {ex1}")

ex2 = Solution().maxCoins([1, 5])
print(f"{ex2==10}, result {ex2}")
