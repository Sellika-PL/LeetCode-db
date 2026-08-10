class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        '''prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total = 0

        k = min(len(prices), len(discounts))

        for i in range(k):
            total += prices[i] * (100 - discounts[i]) / 100

        for i in range(k, len(prices)):
            total += prices[i]

        return total
        '''
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        k = min(len(prices), len(discounts))

        for i in range(k):
            prices[i]= prices[i] * (100 - discounts[i]) / 100

        return sum(prices)
        