class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            area = abs(i - j) * min(heights[i], heights[j])
            max_area = max(area, max_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j-= 1
        return max_area 