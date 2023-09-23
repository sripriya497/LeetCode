class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        j = 0
        vowel = ['a','e','i','o','u']
        while j < k:
            if s[j] in vowel:
                count+=1
            j+=1
        cv = count
        for w in range(k,len(s)):
            if s[w] in vowel:
                count+=1
            if s[w-k] in vowel:
                count-=1
            cv = max(cv, count)
        return cv