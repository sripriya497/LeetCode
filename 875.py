class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low, high = 1, max(piles)
        while high > low:
            mid = (low + high) / 2
            if sum((i+mid-1)/mid for i in piles) > h:
                low = mid+1
            else:
                high = mid
        return low
                