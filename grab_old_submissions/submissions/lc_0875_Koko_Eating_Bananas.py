from math import ceil
def compute_hours_to_eat_all(piles,k):
    hours = sum([ceil(pile / k) for pile in piles])
    return hours
    '''
    hours = 0
    for pile in piles:
        hours += pile/k
    '''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # I think it's important to think about when I want the while loop to
        # terminate and which of the three (left, right, mid)
        # to return. 
        # Here I tried to make left go to exactly the start of the list
        # and I don't think that's what's happened. Instead I believe both converge
        # to the value right before, maybe because of an inversing issue?
        left = 1
        right = 1000000000
        while left <= right:
            mid = (right + left) // 2
            hours_to_eat = compute_hours_to_eat_all(piles,mid)
            if hours_to_eat > h:
                left = mid + 1
            elif hours_to_eat <= h:
                right = mid - 1
        return right + 1