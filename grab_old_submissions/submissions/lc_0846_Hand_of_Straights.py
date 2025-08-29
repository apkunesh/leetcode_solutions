#Missed "edge case" where groupSize is 1. Should have been obvious, oops

from collections import defaultdict
from heapq import heapify, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Case 1: cards can't be pigeonholed
        if len(hand) % groupSize != 0:
            return False
        
        # Idea: basically nlogn
        # Create dict mapping rank to count (O(n) time, O(n) space)
        # Heapify keys (O(n)), pop lowest (O(logn))
        # Check presence of next groupSize-1, decrement all
        # If count would drop to -1, return false
        # Progressively pop from the heap and check, decrement
        rank_counter = defaultdict(int)
        for num in hand:
            rank_counter[num]+=1
        card_count = len(hand)
        heapify(hand)
        group_count = 0
        min_card = None
        while card_count > 0:
            group_count+=1
            if group_count == 1:
                found = False
                # Find a starter
                while not found:
                    candidate = heappop(hand)
                    if rank_counter[candidate] != 0:
                        min_card = candidate
                        rank_counter[candidate]-=1
                        found = True
            elif group_count<=groupSize:
                # Adding along
                next_card_index = min_card+group_count-1
                rank_counter[next_card_index]-=1
                if rank_counter[next_card_index]<0:
                    return False
            if group_count == groupSize:
                group_count=0
            card_count-=1
        return True
                