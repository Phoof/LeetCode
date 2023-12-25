class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1, rowIndex + 1):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(ans[i - 1][j - 1] + ans[i -1][j])
            temp.append(1)
            ans.append(temp)
        return ans[rowIndex]