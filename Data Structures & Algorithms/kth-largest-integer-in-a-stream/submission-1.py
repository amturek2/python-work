class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
    # build a min heap with the nums 
    # erase until the length is k --> then you have the top k elements 
        self.k, self.heap = k, nums 
        heapq.heapify(self.heap)
        print(self.heap)
        while (len(self.heap) > k): 
            heapq.heappop(self.heap)
        print(self.heap)


    def add(self, val: int) -> int:
        # add the value: 
        heapq.heappush(self.heap, val)
        # heappop a value 
        if (len(self.heap) > self.k):
            heapq.heappop(self.heap)
            
        # return top 
        return self.heap[0]
