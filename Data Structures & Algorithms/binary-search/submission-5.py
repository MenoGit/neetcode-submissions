class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <=right:
            middle = (left + right) // 2
            middle_value = nums[middle]

            print(f"middle value={middle_value} index={middle}")
            if middle_value == target:
                return middle
            elif middle_value > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

