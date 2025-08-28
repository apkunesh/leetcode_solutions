from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Set up initial window
        L, window_element_count, max_heap, maxes = (
            0,
            defaultdict(int),
            [-elem for elem in nums[0:k]],
            [],
        )
        heapify(max_heap)
        for elem in max_heap:
            window_element_count[-elem] += 1
        # Scan and append maxes to output
        for R in range(k - 1, len(nums)):
            max_found = None
            while True:
                if window_element_count[-max_heap[0]] > 0:
                    maxes.append(-max_heap[0])
                    break
                else:
                    heappop(max_heap)  # No longer in the window
            if R == len(nums) - 1:  # We don't shift if we're at the edge.
                continue
            # Shift window to the right
            window_element_count[nums[L]] -= 1
            L += 1
            window_element_count[nums[R + 1]] += 1
            heappush(max_heap, -nums[R + 1])
        return maxes
