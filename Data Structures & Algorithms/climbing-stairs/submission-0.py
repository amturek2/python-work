class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2: 
            return 2
        waysToTop = [0] * n 
        waysToTop[n-1] = 1 
        waysToTop[n-2] = 2
        for i in range(n - 3, -1, -1): 
            waysToTop[i] = waysToTop[i + 2] + waysToTop[i + 1]
      
        return waysToTop[0]
