class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = 0
        height = 0
        while i < j:
            distance = j - i
            if heights[i] <= heights[j]:
                height = heights[i]
                i += 1
            else:
                height = heights[j]
                j -= 1
            area = distance * height

            if area > res:
                res = area
        return res 