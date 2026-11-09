class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])

        for i in range(2,len(cost)):
            constaint_one = dp[i-1] + cost[i]
            constaint_two = dp[i-2] + cost[i]
            dp.append(min(constaint_one,constaint_two))
        
        return min(dp[-1],dp[-2])