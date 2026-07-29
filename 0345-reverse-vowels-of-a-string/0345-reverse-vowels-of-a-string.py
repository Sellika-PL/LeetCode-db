class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u','A','E','I','O','U']

        s = list(s)

        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] in v and s[r] in v:
                t = s[l]
                s[l] = s[r]
                s[r] = t

                l += 1
                r -= 1

            elif s[l] not in v:
                l += 1

            else:
                r -= 1

        return "".join(s)