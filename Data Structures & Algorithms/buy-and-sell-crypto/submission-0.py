class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0
        min_price=float("inf")
        for price in prices:
            min_price=min(min_price, price)
            max_prof=max(max_prof, price-min_price)
        return max_prof