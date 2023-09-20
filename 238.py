class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        z = 0
        answer = []
        for i in nums:
            if i != 0:
                p = p*i
            else:
                z += 1
        
        for i in nums:
            if z >= 2:
                answer.append(0)
            elif z == 1 and i != 0:
                answer.append(0)
            elif i == 0:
                answer.append(p)
            else:
                answer.append(p/i)
        return answer