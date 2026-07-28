class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Max heap (using negative values)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        total_sum = sum(target)

        while True:
            # Get the largest element
            largest = -heapq.heappop(max_heap)
            rest = total_sum - largest

            # Base cases
            if largest == 1 or rest == 1:
                return True

            # Invalid situations
            if rest == 0 or largest <= rest:
                return False

            prev = largest % rest

            if prev == 0:
                return False

            # Update sum and heap
            total_sum = rest + prev
            heapq.heappush(max_heap, -prev)