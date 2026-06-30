class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0] 
        if n == 2: 
            return min(cost[0], cost[1])
        # fill in right to left 
        costToTop = [0] * n
        costToTop[n-1] = cost[n-1] 
        costToTop[n-2] = cost[n-2]
        for i in range(n - 3, -1, -1): 
            climb1 = cost[i] + costToTop[i+1]
            climb2 = cost[i] + costToTop[i+2]
            if i == 0: 
                costToTop[i] = min(climb1, climb2, costToTop[i+1])
            else:
                costToTop[i] = min(climb1, climb2)
        return costToTop[0]