class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        result = []
        
        potions.sort()
        for i in spells:
            target = (success - 1) // i
            index = bisect.bisect_right(potions,target)
            count = len(potions) - index
            result.append(count)
        return result
            