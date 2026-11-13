class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We must first binary search the lists
        # Check if the number is in the list of the l and r pointer
        # If it is not, then do the binary search. 
        # When the list is found where the target is in the list, perform binary search in that list
        def binarySearch(checkList: List, target:int) -> bool:
            l = 0
            r = len(checkList) - 1
            while l <= r:
                checkIndex = l + ((r-l)//2)
                checkNum = checkList[checkIndex]
                if checkNum < target:
                    l = checkIndex + 1
                elif checkNum > target:
                    r = checkIndex - 1
                else:
                    return True
            return False

        l = 0
        r = len(matrix) - 1
        while l <= r:
            if target > matrix[l][0] and target < matrix[l][-1]:
                return binarySearch(matrix[l], target)
            if target > matrix[r][0] and target < matrix[r][-1]:
                return binarySearch(matrix[r], target)
            else:
                checkIndex = l + ((r-l)//2)
                if matrix[checkIndex][0] > target:
                    r = checkIndex - 1
                elif matrix[checkIndex][-1] < target:
                    l = checkIndex + 1
                else:
                    return binarySearch(matrix[checkIndex], target)
        return False