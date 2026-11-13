class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            middle = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/middle)
            if hours <= h:
                r = middle
            else:
                l = middle + 1
        return r
        