from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq, rq = deque(), deque()
        lens=len(senate)
        for i in range(lens):
            if senate[i] == 'R':
                rq.append(i)
            else:
                dq.append(i)
        while rq and dq:
            if rq[0] < dq[0]:
                rq.append(lens+rq[0])
            else:
                dq.append(lens+dq[0])
            rq.popleft()
            dq.popleft()
        return 'Radiant' if rq else 'Dire'
                    