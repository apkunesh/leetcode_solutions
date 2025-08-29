class OpenNode:
    # Made a mistake here around the modularity of my recursive logic. I tried to apply my base condition twice,
    # essentially, at the same (top) level, and this was incorrect and led to missing cases.
    def __init__(self,L,R):
        self.L = L
        self.R = R
        self.right = None
        self.left = None
    
    def book(self,L,R):
        if L < self.L or R > self.R:
            return False # New L,R do not match up with any free time
        if self.left is None: 
            # At a leaf, and L,R do indeed match up with free time.
            self.left = OpenNode(self.L,L)
            self.right = OpenNode(R,self.R)
            return True
        # Remaining case: not at a leaf, but L and R are inside current range
        return self.left.book(L,R) or self.right.book(L,R)

class MyCalendar:

    def __init__(self):
        self.root = OpenNode(0,10**9)

    def book(self, startTime: int, endTime: int) -> bool:
        return self.root.book(startTime,endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)