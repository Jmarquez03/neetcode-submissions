class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        result = []
        for i in range(len(nums)):
            num = nums[i]
            search = target - num
            if search in numdict:
                result.append(numdict[search])
                result.append(i)
            else:
                numdict[nums[i]] = i
        return result