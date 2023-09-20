class Solution:
    def reverseWords(self, s: str) -> str:
        aftersplit=s.split()
        return ' '.join(aftersplit[::-1])