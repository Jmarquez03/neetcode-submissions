class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        windowSize = len(s1)
        count = Counter(s1)
        l = 0
        r = l + windowSize
        while r < len(s2) + 1:
            if Counter(s2[l:r]) != count:
                l += 1
                r += 1
            else:
                return True
        return False