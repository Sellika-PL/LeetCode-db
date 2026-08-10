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
        '''prices.sort(reverse=True)
        discounts.sort(reverse=True)

        k = min(len(prices), len(discounts))

        for i in range(k):
            prices[i]= prices[i] * (100 - discounts[i]) / 100

        return sum(prices)'''

        prices.sort()
        discounts.sort()

        k = min(len(prices), len(discounts))
        i=-1
        j=-1

        for _ in range(k):
            amt= prices[i] * (100 - discounts[j]) / 100
            prices[i]=amt
            i-=1
            j-=1

        return sum(prices)


        