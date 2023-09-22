class Solution:
    def maxOperations(self, nums, k):
        counter = Counter(nums)
        count = 0
        for num in nums:
            target = k - num
            if num == target and counter[num] >= 2:
                count += 1
                counter[num] -= 2
            elif num != target and counter[num] > 0 and counter.get(target,0) > 0:
                count += 1
                counter[num] -= 1
                counter[target] -= 1
        return count