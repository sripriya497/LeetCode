class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while high > low:
            mid = low + (high-low) // 2
            if nums[mid+1] < nums[mid] and nums[mid-1] < nums[mid]:
                return mid
            elif nums[mid+1] > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return low if nums[low]>=nums[high] else high
