class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            return tuple(arr)

        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        
        dic2 = defaultdict(int)
        for i in range(len(grid)):
            col =[]
            for j in range(len(grid)):
                col.append(grid[j][i])
            dic2[convert_to_key(col)] += 1
        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        return ans
        # columns = []
        # ans = 0
        # for i in range(len(grid)):
        #     column = []
        #     for j in range(len(grid)):
        #         column.append(grid[j][i])
        #     columns.append(column)
        # for i in columns:
        #     if i in grid:
        #         ans += grid.count(i)

        # return ans


        