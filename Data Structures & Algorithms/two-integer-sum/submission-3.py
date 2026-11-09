class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            left = target - num
            if left in hashmap:
                return [hashmap.get(left), index]
            hashmap[num] = index
        return []