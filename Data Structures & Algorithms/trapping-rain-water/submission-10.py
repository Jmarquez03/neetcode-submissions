class Solution:
    def trap(self, height: List[int]) -> int:
        # Algorithm Plan
        # 1. Make sure i starts where the first elevation is at
        # 2. start l at i. l will keep moving until the next elevation that is higher than than the previous. 
        # 3. r will start at the end of the list and move to the left until the value to the left of it is lower than the current value. 
        # 4. To calculate the rain, we will use min(height[l], height[r]) - height[i]
        if not height:
            return 0
        rain = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                rain += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                rain += rightMax - height[r]
        return rain
