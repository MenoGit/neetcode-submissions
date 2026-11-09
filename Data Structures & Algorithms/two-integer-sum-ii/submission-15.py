class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers) - 1
        l,r = 0, length 

        while l<r:
            sum = numbers[r] + numbers[l]
            if sum == target:
                return [l+1,r+1]
            if sum> target:
                r = r - 1
            elif sum  < target:
                l = l + 1


