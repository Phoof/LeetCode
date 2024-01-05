class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1, len_2 = len(word1), len(word2)
        ans = ""
        while len_1 > len_2:
            ans += word1[len_1 - 1]
            len_1 -= 1
        while len_2 > len_1:
            ans += word2[len_2 - 1]
            len_2 -= 1
        while len_1:
            ans += word2[len_1 - 1]
            ans += word1[len_1 - 1]
            len_1 -= 1
        return ans[::-1]