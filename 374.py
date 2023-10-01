# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
# 1 2 3 4 5 6 7 8 9 10
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        high,low=n,1
        while high>=low:
            mid = (high+low)//2
            pick=guess(mid)
            #print(pick)
            if pick == -1:
                high=mid-1
            elif pick == 1:
                low=mid+1
            else:
                return mid