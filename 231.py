class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n = bin(n)[2:]
        mask = "1".zfill(len(n))[::-1]
        return mask == n