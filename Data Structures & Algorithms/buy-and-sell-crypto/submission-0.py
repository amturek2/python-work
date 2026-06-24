class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 1: 
            return 0
        l, r = 0, 1

        maxval = 0
        while r < n:  
            maxval = max(maxval, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l, r = r, r + 1
            else: 
                l, r = l, r + 1
        
        return maxval

        # Time Complexity: O(n)
        # Space Complexity: O(1)