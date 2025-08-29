from math import ceil

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # TODO: Make a pass over indices to confirm that you can actually access all these
        sum_stones = sum(stones)
        row = list(range(ceil(sum_stones/2)+1))
        for i in range(len(stones)):
            new_row = []
            for j in range(len(row)):
                tentative_index = j - stones[i]
                if tentative_index>=0:
                    new_row.append(min(row[j],row[tentative_index]))
                else:
                    new_row.append(row[j])
            row = new_row
            print(row)
        difference_given_capacity = row[-1]
        print(difference_given_capacity)
        left = ceil(sum_stones/2) - difference_given_capacity
        right = sum_stones//2 + difference_given_capacity
        return abs(right - left)