class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1=0
        for p2 in range(len(nums)):
            if nums[p1] == 0 and nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            if nums[p1] != 0:
                p1 +=1
        return nums
        