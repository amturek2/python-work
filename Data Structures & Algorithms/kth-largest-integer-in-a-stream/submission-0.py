class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k_val = k 
        self.heap = []
        for n in nums: 
            heapq.heappush(self.heap, -1 * n)

        

    def add(self, val: int) -> int:
        # add and return 
        heapq.heappush(self.heap, -1 *  val)
        kthlarge = heapq.nsmallest(self.k_val, self.heap)
        return kthlarge[-1] * -1
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)