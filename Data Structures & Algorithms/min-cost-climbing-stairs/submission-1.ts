class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost: number[]): number {
        const dp: number[] = [];
        dp[0] = cost[0];
        dp[1] = cost[1];
        for (let i = 2; i<cost.length; i++) {
            const cost1: number = dp[i-1] + cost[i];
            const cost2: number  = dp[i-2] + cost[i];
            if (cost1 > cost2) {
                dp[i] = cost2;
            }
            else {
                dp[i] = cost1;
            }
        }
        if (dp[cost.length-1] > dp[cost.length-2]) {
            return dp[cost.length-2]
        }
        else{
            return dp[cost.length-1]
        }
        
    }
}
