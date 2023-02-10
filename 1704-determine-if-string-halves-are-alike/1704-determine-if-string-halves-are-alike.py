class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s) // 2
        l = s[:n] ; r = s[n:]
        test = 'aeiou'
        ans = 0
        for i in range(len(l)):
            if l[i] in test:
                ans+=1
            if r[i] in test:
                ans -=1
        if not ans: return True
        return False             
