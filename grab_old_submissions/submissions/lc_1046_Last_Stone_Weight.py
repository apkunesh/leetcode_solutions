class MaxHeap():
    # Many, many mistakes, mostly around updating indices after swaps.
    def __init__(self,stones: List[int]):
        self.heap = stones
        self.heapify()
    
    def size(self):
        return len(self.heap)

    def push(self,val):
        print(str(self.heap)+ " -- Now pushing " + str(val) + " to stack.")
        self.heap.append(val)
        i = len(self.heap)-1
        while i>1:
            parent = i//2
            if self.heap[parent] < val:
                self.heap[i]=self.heap[parent]
                self.heap[parent] = val
                i = parent
            else:
                break

    def pop(self):
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()
        heaviest = self.heap[1]
        print(str(self.heap) + " -- Now popping " + str(heaviest) + " from stack.")
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)
        return heaviest

    def percolate_down(self,index):
        max_index = len(self.heap) - 1
        i = index
        found = False
        while not found:
            has_right = 2*i+1 <= max_index
            has_left = 2*i <= max_index
            if (not has_left) and (not has_right):
                # Leaf, no more to do
                found = True
                continue
            curr_weight = self.heap[i]
            right_weight = self.heap[2*i+1] if has_right else 0
            left_weight = self.heap[2*i] if has_left else 0
            if curr_weight >= right_weight and curr_weight >= left_weight:
                # We're in the right spot.
                found = True
                continue
            elif right_weight - left_weight >= 0:
                # Right is bigger than left, so we swap right
                self.heap[i] = right_weight
                self.heap[2*i+1] = curr_weight
                i = 2*i+1
            elif left_weight - right_weight >= 0:
                # Left is bigger than right, so we swap left
                self.heap[i] = left_weight
                self.heap[2*i] = curr_weight
                i=2*i
            else:
                print("This shouldn't be possible.")

    def heapify(self):
        self.heap.append(self.heap[0])
        self.heap[0] = 0
        first_childless = len(self.heap) // 2
        max_index = len(self.heap) - 1
        for i in reversed(range(first_childless+1)):
            if i==0:
                break
            self.percolate_down(i)
        print(str(self.heap) + " -- Heapify complete.")

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = MaxHeap(stones)
        while stone_heap.size() > 2:
            heaviest_stone = stone_heap.pop()
            second_place_stone = stone_heap.pop()
            new_stone = heaviest_stone - second_place_stone
            if not new_stone == 0:
                stone_heap.push(new_stone)
            print("Smashed " + str(heaviest_stone) + " and " + str(second_place_stone) + ", resulting in " + str(new_stone))
        if stone_heap.size() == 2:
            return stone_heap.pop()
        elif stone_heap.size() == 1:
            return 0
        else:
            raise ValueError("Shouldn't be possible to have a size of " + str(stone_heap.size()))