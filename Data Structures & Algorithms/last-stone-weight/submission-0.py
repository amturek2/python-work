class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        maxheap = []
        for s in stones:
            heapq.heappush(maxheap, -s)

        while (len(maxheap) > 1): 
            y = heapq.heappop(maxheap) * -1 
            x = heapq.heappop(maxheap) * -1

            if (x != y): 
                new = y - x
                heapq.heappush(maxheap, -1 * new)

        if (len(maxheap) == 1): 
            return (maxheap[0] * -1)
        return 0