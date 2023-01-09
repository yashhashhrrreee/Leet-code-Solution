class Solution:
    def letterCombinations(self, n: str) -> List[str]:
        if n=='':
            return []
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = [""]
        for digit in n:
            digit = int(digit)            
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for letter in options[digit]:
                    queue.append(curr + letter)
        return queue

        