class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        rowc=collections.Counter(tuple(row) for row in grid)
        for i in range(len(grid)):
            colc=[grid[j][i] for j in range(len(grid))]
            count+=rowc[tuple(colc)]
        return count