class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        for i in range(1, numRows):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(ans[i - 1][j - 1] + ans[i -1][j])
            temp.append(1)
            ans.append(temp)
        return ans