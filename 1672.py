class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for x in accounts:
            if max <= sum(x):
                max = sum(x)
            else:
                continue
        return max
