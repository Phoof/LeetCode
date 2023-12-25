class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in d.values():
                    return False
                d[pattern[i]] = s[i]
        return True