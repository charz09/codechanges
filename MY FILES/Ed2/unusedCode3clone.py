class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        shortest = ""
        mem = [[None for y in range(len(s))] for x in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                k = i + j
                if k >= len(s):
                    break
                if k - j > 1:
                    if mem[j + 1][k - 1] == True and s[j] == s[k]:
                        mem[j][k] = True
                    else:
                        mem[j][k] = False
                elif k - j == 1:
                    if s[j] == s[k]:
                        mem[j][k] = True
                    else:
                        mem[j][k] = False
                else:
                    mem[j][k] = True
                if mem[j][k] and (k - j + 1) > len(longest):
                    longest = s[j:k+1]
        return longest
    def doNothing(self):
        pass
    def doSomething(self):
        pass
