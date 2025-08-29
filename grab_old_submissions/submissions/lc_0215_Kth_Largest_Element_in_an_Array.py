class MaxHeap:
    # First error was an index issue: failed to include root in 
    # percolation by exclusion from while loop
    # Second error fails to take into account small heaps with pop
    def __init__(self,nums):
        self.nums = nums
        self._heapify()

    def _percolate_down(self,index):
        max_index = len(self.nums) - 1
        i = index
        if i == 0:
            # Don't mess with dummy node
            return
        while i>0:
            has_left_child = 2*i <= max_index
            has_right_child = 2*i+1 <= max_index
            if not has_left_child and not has_right_child:
                # We're a leaf!
                return
            left_child_val = self.nums[2*i] if has_left_child else -10000000
            right_child_val = self.nums[2*i+1] if has_right_child else -10000000
            cur_val = self.nums[i]
            if cur_val > left_child_val and cur_val > right_child_val:
                # In correct interior place
                return
            elif left_child_val >= right_child_val:
                # Left is bigger, so we percolate left up
                tmp = self.nums[i]
                self.nums[i] = self.nums[2*i]
                self.nums[2*i] = tmp
                i = 2*i
            elif right_child_val > left_child_val:
                # Right is bigger, so we percolate right up
                tmp = self.nums[i]
                self.nums[i] = self.nums[2*i+1]
                self.nums[2*i+1] = tmp
                i = 2*i+1
            else:
                raise ValueError("You shouldn't be here...")

    def _heapify(self):
        self.nums.append(self.nums[0])
        self.nums[0] = 1000000000
        max_index = len(self.nums) - 1
        first_with_child = max_index//2
        for i in reversed(range(first_with_child + 1)):
            self._percolate_down(i)
    def pop(self):
        if len(self.nums) == 1:
            return None
        elif len(self.nums) == 2:
            return self.nums.pop()
        biggest = self.nums[1]
        self.nums[1] = self.nums.pop()
        self._percolate_down(1)
        return biggest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = MaxHeap(nums)
        for i in range(k):
            cur_max = max_heap.pop()
        return cur_max
        