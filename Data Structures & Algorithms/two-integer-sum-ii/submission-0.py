class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for l in range(len(numbers)):

            r = len(numbers)-1
            while l<r:
                if numbers[l] + numbers[r] == target:
                    return [l+1,r+1]
                else:
                    r = r - 1
