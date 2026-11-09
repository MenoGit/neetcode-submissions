class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights)-1
        l = 0
        total = 0
        while r != l:
            check = (r-l) * min(heights[r],heights[l])
            if total < check:
                total = check
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return total





        