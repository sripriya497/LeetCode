class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            while s and i < 0 and s[-1] >0:
                if s[-1] == -i:
                    s.pop()
                    break
                elif s[-1] > -i:
                    break
                elif s[-1] < -i:
                    s.pop()
            else:
                s.append(i)
        return s