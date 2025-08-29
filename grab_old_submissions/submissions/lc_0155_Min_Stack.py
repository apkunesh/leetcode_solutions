class MinStack:

    def __init__(self):
        self._internal_list = []
        self._min_stack = []
        self._value_counts = {}

    def push(self, val: int) -> None:
        self._internal_list.append(val)
        if (not self._min_stack) or (val < self._min_stack[-1]):
            self._min_stack.append(val)
        if self._value_counts.get(val):
            self._value_counts[val] +=1
        else:
            self._value_counts[val] = 1

    def pop(self) -> None:
        removed_entry = self._internal_list.pop()
        if self._value_counts.get(removed_entry):
            self._value_counts[removed_entry] -= 1
            if self._value_counts[removed_entry] == 0 and removed_entry == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self) -> int:
        return self._internal_list[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()