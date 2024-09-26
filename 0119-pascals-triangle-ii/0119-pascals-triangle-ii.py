class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(rowIndex):
            curr = []
            tmp = [0] + prev + [0]
            for j in range(len(prev) + 1):
                curr.append(tmp[j] + tmp[j + 1])
            prev = curr
        
        return prev
        