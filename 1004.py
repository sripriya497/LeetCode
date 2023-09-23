class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxval = 0
        i = j = 0
        while j < len(nums):
            if nums[j] == 0:
                k-=1
            while k < 0:
                if nums[i] == 0:
                    k+=1
                i+=1
            #print(i,j)
            maxval=max(maxval,j-i+1)
            j+=1
        return maxval
                