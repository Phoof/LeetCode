class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = ""
        count = 0
        for i, l in enumerate(s[::-1]):
            if l == "#":
                count += 1
            else:
                if count == 0:
                    new_s += l
                else:
                    i += 1
                    count -= 1
        new_t = ""
        count = 0
        for i, l in enumerate(t[::-1]):
            if l == "#":
                count += 1
            else:
                if count == 0:
                    new_t += l
                else:
                    i += 1
                    count -= 1
        return new_s == new_t