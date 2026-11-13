class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # if the leftmost number is greater than or equal to the middle number
            if nums[l] <= nums[m]:
                # we move the left if the target is greater than the middle number or if the target is less than the left num
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                # if not, we move the right
                else:
                    r = m - 1
            # if the left number is greater than the middle
            else:
                #We move the right if the target is less then the middle number or if target is geater than the right number
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                # Otherwise, we move the left
                else:
                    l = m + 1
        return -1