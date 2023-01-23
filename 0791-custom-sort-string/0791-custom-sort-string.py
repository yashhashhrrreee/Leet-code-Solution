class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ranking = {v:i for i, v in enumerate(order)}
        rest = ''
        ans = ''
        for x in s:
            if x not in ranking:
                rest += x
                continue
            ans += x
        
        ans = sorted(ans, key = lambda x: ranking[x])
        return ''.join(ans) + rest