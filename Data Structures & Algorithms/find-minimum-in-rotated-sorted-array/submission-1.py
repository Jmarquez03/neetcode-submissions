class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            m = l + (r-l)//2
            num = nums[m]
            if num < nums[l] and num < nums[r]:
                r = m
            elif num > nums[l] and num > nums[r]:
                l = m
            else:
                return min(nums[l], nums[r])
        return nums[r]