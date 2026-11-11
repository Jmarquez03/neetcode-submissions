class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        checked = set()
        if nums == []:
            return 0
        res = 1
        for num in nums:
            count = 1
            if num + 1 not in unique or num in checked:
                continue
            else:
                checked.add(num)
                checkNum = num
                while checkNum + 1 in unique:
                    count += 1
                    checkNum += 1
                    checked.add(checkNum)
                checkNum = num
                while checkNum - 1 in unique:
                    count += 1
                    checkNum -= 1
                    checked.add(checkNum)
                if count > res:
                    res = count
        return res