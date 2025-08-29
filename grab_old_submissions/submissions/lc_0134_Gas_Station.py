class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deltas = [a-b for a,b in zip(gas,cost)]
        if sum(deltas)<0: #O(N)
            return -1
        # Let's try taking double the memory but just a single O(N) (specifically 2N) pass

        starting_index = 0
        i = 0
        total = 0
        while i<len(deltas):
            total+=deltas[i]
            if total<0:
                total=0
                starting_index = i+1
            i+=1
        return starting_index
