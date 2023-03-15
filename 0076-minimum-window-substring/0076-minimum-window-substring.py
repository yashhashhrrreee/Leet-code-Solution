class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        tCount = len(tCounter)
        l, r = 0, 0
        curWindowCount = 0
        maxl, maxr = 0, float("inf")
        curWindow = {}
        
        while r < len(s):
            if s[r] in tCounter:
                curWindow[s[r]] = 1 + curWindow.get(s[r], 0)
                if curWindow[s[r]] == tCounter[s[r]]:
                    curWindowCount +=1
            while curWindowCount == tCount:
                if (r-l) < (maxr - maxl):
                    maxl, maxr = l, r
                if s[l] in tCounter:
                    if curWindow[s[l]] == tCounter[s[l]]:
                        curWindowCount -=1
                    curWindow[s[l]] -=1
                l +=1
            r +=1
        return s[maxl:maxr+1] if maxr != float("inf") else ""