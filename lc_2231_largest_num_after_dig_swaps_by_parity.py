from heapq import heappush, heappop


class Solution:
    def largestInteger(self, num: int) -> int:
        # First thought: just get all the evens and odds in lists, sort, and traverse according to index maps
        even_nums, odd_nums, even_tens_powers, tens_power = [], [], set(), 0
        while num > 0:
            remainder = num % 10
            if remainder % 2 == 0:
                heappush(even_nums, remainder)
                even_tens_powers.add(tens_power)
            else:
                heappush(odd_nums, remainder)
            tens_power, num = tens_power + 1, num // 10
        tens_power, result = 0, 0
        while even_nums or odd_nums:
            result += (
                heappop(even_nums) * 10**tens_power
                if tens_power in even_tens_powers
                else heappop(odd_nums) * 10**tens_power
            )
            tens_power += 1
        return result
