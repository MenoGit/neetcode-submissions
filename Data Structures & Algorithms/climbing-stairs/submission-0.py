class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)
        for i in range(3,n+1):
            steps = dp[i-1] + dp[i-2]
            dp.append(steps)
        
        return dp[n]
