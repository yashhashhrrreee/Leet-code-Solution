class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        hashed = set(words)
        answer = set()
        for index in range(len(words)):
            dp = [0]*(31)
            word = words[index]
            n = len(word)
            for left in range(n-1, -1, -1):
                for right in range(left, n + 1):
                    if word[left:right] in hashed and (dp[right] > 0 or right == n):
                        dp[left] = max(dp[left], 1 + dp[right])
            if dp[0] >= 2:
                answer.add(word)
        return answer
    
    