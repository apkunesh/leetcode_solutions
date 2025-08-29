from collections import defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Don't forget to - the heappush
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        freq_and_num = []
        for key,val in frequency.items():
            freq_and_num.append((-val,key))
        heapify(freq_and_num)
        result = []
        for i in range(k):
            result.append(heappop(freq_and_num)[1])
        return result