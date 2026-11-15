class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newList = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if newList[i] == newList[i + 1]:
                return newList[i]
            else:
                i += 1
        return 0