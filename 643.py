class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        j = 0
        total = 0
        arr = []
        while j < k:
            total+=nums[j]
            j+=1
        arr.append(total)
        for i in range(1,len(nums)-k+1):
            total=total-nums[i-1]+nums[i+k-1]
            arr.append(total)
        maxval=max(arr)
        return round(maxval/k,5)