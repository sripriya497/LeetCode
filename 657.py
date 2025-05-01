class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = [move for move in moves]
        md = dict(Counter(moves))
        return md.get('U',0) == md.get('D',0) and md.get('L',0) == md.get('R',0)
