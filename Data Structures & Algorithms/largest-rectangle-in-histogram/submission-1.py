class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        maxArea = 0
        # We will be storing (index, height) pairs
        stack = []
        # We will keep track of the index and height
        for i, h in enumerate(heights):
            # start which will be used for calculating area
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                # Compute Area and assign to max if greater than
                maxArea = max((i - ind) * height, maxArea)
                start = ind
            stack.append((start, h))
        while stack:
            ind, height = stack.pop()
            maxArea = max(height * (len(heights) - ind), maxArea)
        return maxArea
