class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        i, j = n-1,  m-1
        wildcard_backtracking = []
        while i >=0:
            # single char case
            if j >= 0 and (p[j] == '.' or p[j] == s[i]):
                i-=1
                j-=1 
            elif j >= 0 and p[j] == '*':
                if p[j-1] == '.' and j == 1:
                    return True
                else:
                    j-=2
                    wildcard_backtracking.append((p[j+1], j,i))                 
            elif len(wildcard_backtracking) > 0:
                p_back, j_back, i_back = wildcard_backtracking.pop()
                i, j = i_back, j_back
                if p_back == '.' or p_back == s[i]:
                    i-=1
                    wildcard_backtracking.append((p_back, j_back, i))
            else:
                return False
        while j >= 0 and p[j] == '*':
            j-=2
        return i == -1 and j == -1