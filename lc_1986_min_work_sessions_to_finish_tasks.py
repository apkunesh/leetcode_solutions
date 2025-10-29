from collections import Counter
from typing import List

# Bad intuition from previous failing attempt. This allows waste, as it does not optimize minimal empty time at the end of a session.
"""
My intuition is that we can do this greedily, which is to say that we can sort
the tasks and fill 'em in wherever they fit + earliest. Let's see if I can form a counterexample.
sessionTime =  4, tasks =[2,3,2,1,1]
I'd fill with [[3,1],[2,2],[1]]
What about something like 6, [4,4,3,3,3,2]?
result would look like [[4,2],[4],[3,3],[3]],
built as [[4]] -> [[4],[4]] ->  [[4],[4],[3]] -> [[4],[4],[3,3]] -> [[4],[4],[3,3],[3]] -> [[4,2],[4],[3,3],[3]]
So I think this works...
However, how can I cleanly match a value to its best spot?
I think I can pull from a maxheap on remaining size. I *think* this will still be optimal.
"""


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # New idea: after sorting, we try to find entries which result in 0 waste.
        # If we cannot find such a choice, we move on.
        # This could get really slow. Not greedy, at all, really.
        num_counts = Counter(tasks)
        selectable_times = list(num_counts.keys())

        return 0


soln = Solution().minSessions

print(f"{soln([3,1,3,1,1],8)} should be 2")
print(f"{soln([1,2,3],3)} should be 2")
print(f"{soln([1,2,3,4,5],15)} should be 1")
