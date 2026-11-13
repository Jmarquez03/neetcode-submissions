class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            checkInd = l + int((r - l)/2)
            checkNum = nums[checkInd]
            if checkNum > target:
                r = checkInd - 1
            elif checkNum < target:
                l = checkInd + 1
            else:
                return checkInd
        return -1