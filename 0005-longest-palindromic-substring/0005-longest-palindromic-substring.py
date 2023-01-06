class Solution:
    def palindrome(self, s, l, r):
        while (l >= 0 and r < len(s) and
                s[l] == s[r]):
            l-=1
            r+=1
        return s[l+1:r]


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        for i in range(n):
            p1 = self.palindrome(s, i, i)
            p2 = self.palindrome(s, i, i+1)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
            # print(i, p1, p2)
        return longest
        