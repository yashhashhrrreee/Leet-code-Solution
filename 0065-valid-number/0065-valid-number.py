class Solution:
    def isNumber(self, s: str) -> bool:
        currState = 0
        dfa = [
            { 'digit': 1, 'dot': 5, 'sign': 6 },
            { 'digit': 1, 'dot': 2, 'eE': 3 },
            { 'digit': 2, 'eE': 3 },
            { 'sign': 7, 'digit': 8 },
            { 'digit': 4, 'eE': 3 },
            { 'digit': 4 },
            { 'dot': 5, 'digit': 1 },
            { 'digit': 8 },
            { 'digit': 8 }
        ]

        for c in s:
            # print(c)
            if c <= "9" and c >= "0":
                c = 'digit'
            elif c == "e" or c == "E":
                c = 'eE'
            elif c == ".":
                c = 'dot'
            elif c == "-" or c == "+":
                c = 'sign'
            # print(c)
            # print(currState)
            if c in dfa[currState]:
                # print(currState)
                currState = dfa[currState][c]
                # print(currState)
            else:
                return False

        # print(currState)
        return currState in (1,2,4,8)