from collections import defaultdict
from collections import deque
from heapq import heapify, heappush,heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Fresh mistake: did not recall that heapify is in-place.
        # TODO: Consider edge cases (only 1 task, n=0)
        counts = defaultdict(int)
        for task in tasks:
            counts[task]+=1
        heap = [-elem for elem in counts.values()] # Note negative
        heapify(heap)
        queue = deque([None]*n)
        n_items_in_queue,length = 0,0
        while n_items_in_queue>0 or heap:
            if heap:
                count = heappop(heap)
                if count < -1:
                    queue.append(count+1)
                    n_items_in_queue+=1
                else:
                    queue.append(None)
            else:
                queue.append(None)
            count_to_include = queue.popleft()
            if count_to_include is not None:
                n_items_in_queue-=1
                heappush(heap,count_to_include)
            length += 1
        return length
