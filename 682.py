class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for x in operations:
            if x not in ['+','D','C']:
                l.append(x)
            elif x == 'C':
                cnt = len(l)
                l = l[:cnt-1]
            elif x == '+':
                l.append(int(l[-1]) + int(l[-2]))
            elif x == 'D':
                l.append(2 * int(l[-1]))
        return sum([int(y) for y in l])

