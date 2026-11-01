class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0

        for r in range(len(s)):
            i = s.find(s[r], l, r)
            if i != -1:
                l = i + 1
            res = max(res, r - l + 1)

        return res