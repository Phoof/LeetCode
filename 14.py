class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        found = False
        if len(strs) == 1:
            return strs[0]
        elif not strs:
            return ""
        while not found:
            if min_len == 0:
                return ""
            temp = strs[0][:min_len]
            for s in strs[1:]:
                if s[:min_len] != temp:
                    min_len -= 1
                    found = False
                    break
                found = True
        return strs[0][:min_len]