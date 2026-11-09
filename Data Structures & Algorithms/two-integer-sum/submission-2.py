class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            output = target - value
            if output in hashmap:
                return [hashmap[output],index]
            hashmap[value] = index

