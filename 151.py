class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")[::-1]
        s = list(filter(None, s))
        return " ".join(s)