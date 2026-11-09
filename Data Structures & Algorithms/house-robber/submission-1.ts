class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        const dp: number[] = [];
        dp[0] = 0;
        dp[1] = nums[0];
        const length: number = nums.length;
        for(let i=2; i<=length; i++) {
            const take: number = nums[i-1] + dp[i-2];
            const skip: number = dp[i-1];
            if (take>skip) {
                dp[i] = take;
            }
            else{
                dp[i] = skip;
            }
        }
        return dp[nums.length]
    }
}
