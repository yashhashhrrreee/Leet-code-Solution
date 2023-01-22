class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPlaindrome(s, lp, rp):
            while lp < rp:
                if s[lp] != s[rp]:
                    return False
                lp, rp = lp+1, rp-1
            return True
        
        n = len(s)
        dp = {n:[]}
        def getPalPart(pos):
            nonlocal n
            if pos in dp:
                return dp[pos]
            
            possPartition = []
            for i in range(pos, n):
                if not isPlaindrome(s, pos, i):
                    continue
                partitions = getPalPart(i+1)
                for part in partitions:
                    possPartition.append([s[pos:i+1]] + part)
            else:
                if isPlaindrome(s, pos, n-1):
                    possPartition.append([s[pos:]])
            dp[pos] = possPartition
            return dp[pos]
        
        return getPalPart(0)