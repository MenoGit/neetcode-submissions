class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        dp.append(0)
        dp.append(nums[0])
        for i in range(2,len(nums)+1):
            take = dp[i-2] + nums[i-1]
            skip = dp[i-1]
            dp.append(max(take,skip))
        print(dp)
        return dp[-1]
