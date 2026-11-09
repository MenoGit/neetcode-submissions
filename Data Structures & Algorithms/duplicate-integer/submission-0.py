class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for value in nums:
            if value in hashmap:
                return True
            hashmap.add(value)
        return False