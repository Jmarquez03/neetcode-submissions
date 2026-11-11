class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        target = 0
        i = 0
        j = i + 1
        k = len(sortedNums) - 1
        while j < k:
            while j < k:
                total = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if total > target:
                    k -= 1
                elif total < target: 
                    j += 1
                else:
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    k -= 1
                    while sortedNums[k] == sortedNums[k + 1] and k > 0:
                        k -= 1
                    j += 1
                    while sortedNums[j] == sortedNums[j - 1] and j < len(sortedNums) - 1:
                        j += 1
            i += 1
            while sortedNums[i] == sortedNums[i - 1] and i < len(sortedNums) - 2:
                i += 1
            j = i + 1
            k = len(sortedNums) - 1
        return res
