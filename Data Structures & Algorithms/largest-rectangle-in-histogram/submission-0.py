class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Ideas:
        #   Inverted version of rainwater?
        if not heights:
            return 0
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxArea = max(maxArea, height * (i - ind))
                start = ind
            stack.append((start, h))
        while stack:
            ind, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - ind))
        return maxArea
