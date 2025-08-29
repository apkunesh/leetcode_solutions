from heapq import heappush, heappop
class TwoHeap():
    def __init__(self):
        self.small,self.large = [],[]
    
    def add(self,val):
        if self.small:
            if val>-self.small[0]:
                heappush(self.large,val)
            else:
                heappush(self.small,-val)
        elif self.large:
            if val < self.large[0]:
                heappush(self.small,-val)
            else:
                heappush(self.large,val)
        else:
            heappush(self.small,-val)
        if len(self.large) > len(self.small)+1:
            heappush(self.small,-heappop(self.large))
        elif len(self.small) > len(self.large)+1:
            heappush(self.large,-heappop(self.small))
    
    def remove(self,val):
        if val <= -self.small[0]:
            heap = self.small
            val = -val
        else:
            heap=self.large
        found = None
        for i in range(len(heap)):
            if heap[i] != val:
                continue
            found = i
            break
        old = found
        while old > 0:
            next_swap = ((old+1)//2)-1
            dummy = heap[old]
            heap[old] = heap[next_swap]
            heap[next_swap] = dummy
            old = next_swap
        removed = heappop(heap)
        if len(self.small) > len(self.large) +1:
            heappush(self.large,-heappop(self.small))
        elif len(self.large) > len(self.small)+1:
            heappush(self.small,-heappop(self.large))
    
    def median(self):
        if len(self.small)>len(self.large):
            return -self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        return (self.large[0]-self.small[0])/2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        results = []
        two_heap = TwoHeap()
        for i in range(k):
            two_heap.add(nums[i])
        results.append(two_heap.median())
        for i in range(k,len(nums)):
            to_remove = i-k
            two_heap.remove(nums[to_remove])
            two_heap.add(nums[i])
            results.append(two_heap.median())
        return results