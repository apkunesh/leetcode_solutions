from collections import defaultdict
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        # NOTE: Idea: map from digit to count of digits.
        # Then we can move from 1-9 and, at each of 3 layers, append legal values.
        # This is "exhaustive" in a sense, but is only ever 1000 computations.
        digit_count = defaultdict(int)
        for digit in digits:
            digit_count[digit] += 1
        global_result, local_result = [], []
        for i in range(1, 10):
            if digit_count[i] < 1:
                continue
            local_result.append(i)
            digit_count[i] -= 1
            for j in range(10):
                if digit_count[j] < 1:
                    continue
                local_result.append(j)
                digit_count[j] -= 1
                for k in range(0, 10, 2):
                    if digit_count[k] < 1:
                        continue
                    global_result.append(
                        local_result[0] * 100 + local_result[1] * 10 + k
                    )
                digit_count[local_result.pop()] += 1
            digit_count[local_result.pop()] += 1
        return global_result
