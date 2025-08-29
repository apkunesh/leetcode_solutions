from heapq import heapify, heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_to_profits = [(cost,benefit) for cost,benefit in zip(capital,profits)]
        heapify(capital_to_profits)
        current_money = w
        profits_heap = [] # Negative, make sure to reverse signs
        for i in range(k):
            while len(capital_to_profits)>0 and capital_to_profits[0][0] <= current_money:
                heappush(profits_heap,-heappop(capital_to_profits)[1])
            if len(profits_heap) == 0:
                return current_money
            current_money = current_money - heappop(profits_heap)
        return current_money