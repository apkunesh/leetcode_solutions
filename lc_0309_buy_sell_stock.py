from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_cache = {}

        def recurse(i, has_stock):
            cache_key = (i, has_stock)
            if i >= len(prices):
                return 0
            if cache_key in profit_cache:
                return profit_cache[cache_key]
            wait = recurse(i + 1, has_stock)
            if not has_stock:
                action = recurse(i + 1, not has_stock) - prices[i]
            else:
                action = recurse(i + 2, not has_stock) + prices[i]
            profit_cache[cache_key] = max(wait, action)
            return profit_cache[cache_key]

        return recurse(0, False)
