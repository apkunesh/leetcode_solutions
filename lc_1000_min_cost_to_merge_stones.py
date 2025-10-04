from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        # Note that with 4, 2, 4->3->2->1
        # While with 4,3, 4->2->XX
        # and with 4,3 5->3->1 xx
        # With 8,4, 8 -> 5 -> 2 XX
        # Mean while 10,4 gives 10->7->4->1
        # -> (len(stones)-1)%k==0 or else we return -1.
        if (len(stones) - 1) % (k - 1) != 0:
            return -1
        stones = [0] + stones + [0]
        # Now we consider L and R outer stones as the "last to be merged" and find the min inside. Note that the dummy stones find us a minimum score.
        partial_sum = [0]
        for i in range(1, len(stones)):
            partial_sum.append(partial_sum[-1] + stones[i])
            # Value between 0 and 2 is then partial_sum[2-1] - partial_sum[0

        cost_cache = {}

        def recurse(i, j, n_piles):
            if j - i + 1 == n_piles:
                print(
                    f"Exact size found with start at {i} and end at {j} with {n_piles} piles"
                )
                cost_cache[(i, j, k)] = 0
                return cost_cache[(i, j, k)]
            if j - i < k - 1:
                print(
                    f"Distance between {i} and {j} too small for {k} elements; returning inf"
                )
                return float("infinity")
            else:
                big_total_cost = float("infinity")
                for partition in range(i + 1, j):
                    for left_piles in range(1, k):
                        right_piles = k - left_piles
                        print(
                            f"Attempting to split from {i} to {j} at index {partition} into {left_piles} left and {right_piles} right piles"
                        )
                        left_cost = recurse(i, partition - 1, left_piles)
                        right_cost = recurse(partition, j, right_piles)
                        print(f"Left and right costs are {left_cost} and {right_cost}")
                        big_total_cost = min(
                            big_total_cost,
                            left_cost
                            + right_cost
                            + partial_sum[j - 1]
                            - partial_sum[i],
                        )
                cost_cache[(i, j, k)] = big_total_cost
                return cost_cache[(i, j, k)]

        # Basically I need "what's the cost to condense the stuf inside into 2 piles"
        recurse(0, len(stones), 1)
        print(cost_cache)
        return cost_cache[(1, len(stones) - 1)]


print(f"{Solution().mergeStones([3,2,4,1],2)} should be 20")
print(f"{Solution().mergeStones([3,2,4,1],3)} should be -1")
print(f"{Solution().mergeStones([3,5,2,1,6],3)} should be 20")

"""
Input: stones = [3,2,4,1], k = 2
Output: 20

Input: stones = [3,2,4,1], k = 3
Output: -1


Input: stones = [3,5,1,2,6], k = 3
Output: 25

"""
