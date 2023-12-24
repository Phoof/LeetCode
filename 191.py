class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        def bitMask(n, mask):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if (n & mask) == 1:
                return 1 + bitMask(n >> 1, mask)
            else:
                return bitMask(n >> 1, mask)
        return bitMask(n, mask)