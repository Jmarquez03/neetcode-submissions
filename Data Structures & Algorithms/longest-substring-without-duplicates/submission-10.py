class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        l = 0
        maxLength = 0
        for r in range(len(s)):
            if s[r] in check:
                l = max(check[s[r]] + 1, l)
            check[s[r]] = r
            maxLength = max(maxLength, r-l+1)
        return maxLength