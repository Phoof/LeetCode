class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for n in digits:
            s += str(n)
        s = int(s) + 1
        return [int(d) for d in str(s)]