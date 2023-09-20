class Solution:
    def reverseVowels(self, s: str) -> str:
        lens=len(s)
        s=[x for x in s]
        i = 0
        j = lens-1
        while i<j:
            if s[i] not in ['a','e','i','o','u','A','E','I','O','U']:
                i+=1
            elif s[j] not in ['a','e','i','o','u','A','E','I','O','U']:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return str(''.join(s))
            