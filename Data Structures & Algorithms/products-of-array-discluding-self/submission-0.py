class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        store = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            store[i] = prefix
            prefix = prefix * nums[i]
        postfix =  1
        for i in range(len(nums) -1,-1,-1):
            store[i] = postfix * store[i]
            postfix = nums[i] * postfix
        return store

