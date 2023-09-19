class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        l1=len(str1)
        l2=len(str2)
        while l1 != l2:
            if l1 > l2:
                l1-=l2
            else:
                l2-=l1
        return str1[:l1]