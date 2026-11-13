class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            middle = (l + r)//2
            most_bananas = 0
            for pile in piles:
                most_bananas += math.ceil(pile/middle)
            if most_bananas <= h:
                r = middle
            else:
                l = middle + 1
        return r 