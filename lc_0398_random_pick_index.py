from collections import defaultdict
from random import choice
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self._num_to_index = defaultdict(list)
        for i in range(len(nums)):
            self._num_to_index[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return choice(self._num_to_index[target])
