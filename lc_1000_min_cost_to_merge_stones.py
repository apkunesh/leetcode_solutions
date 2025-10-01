from typing import List


def update_partition(partition_in, k) -> List:
    print(f"Updating {partition_in}")
    partition_index = len(partition_in) - 1
    count = 0
    while partition_index > 0:
        print("Part ind is ", partition_index)
        left_max = len(partition_in) - 1 - count
        tent = partition_in[partition_index] + k - 1
        if tent > left_max:
            count += 1
            partition_index -= 1
            continue
        count = 0
        for i in range(partition_index, len(partition_in)):
            partition_in[i] = tent + count
        print(f"to {partition_in}")
        return partition_in
    return []


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if k > len(stones):
            print("Wrong lenghts")
            return -1
        elif k == len(stones):
            return sum(stones)
        if (len(stones) - 1) % (k - 1) != 0:
            print("Too samll")
            return -1
        # Otherwise it's possible.
        # Let's try to just build this bad boy up from permutations
        sums = {}
        # O(n**2)
        for i in range(len(stones)):
            cur_sum = 0
            for j in range(i, len(stones)):
                cur_sum += stones[j]
                sums[(i, j)] = cur_sum
        min_costs = {(i, i): 0 for i in range(len(stones))}
        :"!"

        def recurse(i, j, level,partition_here):  # We can assume that the i,j here can be cleanly done
            print(f"LEVEL {level}")
            if (i, j) in min_costs:
                print(f"Cache hit at {i,j}: ", min_costs[(i, j)])
                return min_costs[(i, j)] + sums[(i, j)]
            partition_lefts = [i + elem for elem in range(k)]
            local_min = 10**30
            while partition_lefts != []:
                print(f"part lefts: ", partition_lefts)
                part_rights = [elem - 1 for elem in partition_lefts][1:] + [j]
                local_sum = 0
                for left, right in zip(partition_lefts, part_rights):
                    print("Recursing with ", [left, right])
                    local_sum += recurse(left, right, level + 1,partition_lefts)
                local_min = min(local_min, local_sum)
                # Now we update the partition
                partition_lefts = update_partition(partition_lefts, k)
            print(f"Cache create at {i},{j}: ", local_min)
            min_costs[(i, j)] = local_min
            return min_costs[(i, j)] + sums[(i, j)]

        result = recurse(0, len(stones) - 1, 0)
        print(min_costs)
        return result


# Constraints:
#
#     n == stones.length
#     1 <= n <= 30
#     1 <= stones[i] <= 100
#     2 <= k <= 30


soln = Solution()
res1 = soln.mergeStones([3, 2, 4, 1], 2)
assert res1 == 20, res1
res2 = soln.mergeStones([3, 2, 4, 1], 3)
assert res2 == -1, res2
res3 = soln.mergeStones([3, 5, 1, 2, 6], 3)
assert res3 == 25, res3
