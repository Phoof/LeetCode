class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        ans = temp = 0
        for l in s:
            counts[l] = counts.get(l, 0) + 1
        for k, v in counts.copy().items():
            if v > 1:
                if v % 2 == 0:
                    ans += v
                else:
                    ans += v - 1
                    temp = 1
                del(counts[k])
        if counts:
            return ans + 1
        return ans + temp