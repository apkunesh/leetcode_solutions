class Heap:
    # Made some typos but the concept was correct. May help to be extra-verbal here.
    # Made one major conceptual mistake: didn't update the
    # index of the "tail-swapped" down-percolating value when popping.
    def __init__(self,k):
        self.heap = [-9999999]
        self.size_limit = k
    
    def push(self,val):
        if len(self.heap) == 1:
            self.heap.append(val)
            return self.heap[1]
        if val < self.heap[1] and len(self.heap) > self.size_limit:
            return self.heap[1]
        self.heap.append(val)
        index = len(self.heap) - 1
        while self.heap[index] < self.heap[index // 2]:
            tmp = self.heap[index]
            self.heap[index] = self.heap[index//2]
            self.heap[index//2] = tmp
            index = index//2
        while len(self.heap) > self.size_limit+1:
            self.pop()
        return self.heap[1]
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        to_return = self.heap[1]
        self.heap[1] = self.heap.pop()
        spot_found = False
        i = 1
        while not spot_found:
            # Establish existence of left and right children
            has_left_child = 2*i <= len(self.heap) - 1
            has_right_child = 2*i+1 <= len(self.heap) - 1
            if not has_right_child and not has_left_child:
                # We're a leaf, end
                spot_found = True
                continue

            # See if left or right child are smaller; 
            # if either are, swap with the minimum
            left_val = self.heap[2*i] if has_left_child else 10000
            right_val = self.heap[2*i+1] if has_right_child else 10000
            should_swap = self.heap[i] > left_val or self.heap[i] > right_val
            if not should_swap:
                spot_found = True
                continue
            tmp = self.heap[i]
            if left_val < right_val:
                #swap left
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = tmp
                i = 2*i
            else:
                # swap right
                self.heap[i] = self.heap[2*i+1]
                self.heap[2*i+1] = tmp
                i = 2*i+1
        return to_return




class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap(k)
        for num in nums:
            self.heap.push(num)

    def add(self, val: int) -> int:
        return self.heap.push(val)