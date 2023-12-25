class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n)[2:].zfill(32))
        n = n[::-1]
        return int(n, 2)