class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = high = float(inf)
        for n in nums:
            if n<=low:
                low = n
            elif n<=high:
                high = n
            else:
                return True
        return False