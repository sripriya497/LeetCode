class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        mx = j = i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k-=1
            while k < 0:
                if nums[i] == 0:
                    k+=1
                i+=1
            mx = max(mx,j-i)
        return mx