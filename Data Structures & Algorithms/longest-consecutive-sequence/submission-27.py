class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0
        for num in nums:
            if num - 1 in unique:
                continue
            else:
                length = 1
                while num + 1 in unique:
                    length += 1
                    num += 1
                if length > res:
                    res = length
        return res