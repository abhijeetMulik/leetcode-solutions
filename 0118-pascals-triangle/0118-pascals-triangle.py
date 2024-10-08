class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            tmp = [0] + ans[-1] + [0]
            row = []
            for j in range(len(ans[-1]) + 1):
                row.append(tmp[j] + tmp[j + 1])
            ans.append(row)
        return ans

        