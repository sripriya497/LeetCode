class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        high=max(candies)
        candylen=len(candies)
        
        for j in range(candylen):
            if candies[j]+extraCandies < high:
                result.append(False)
            else:
                result.append(True)
        return result