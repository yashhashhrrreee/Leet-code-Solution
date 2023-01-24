class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        di = dividend
        do = divisor
        if di > 0 and do > 0 :
            return di // do
        elif do < 0 and di > 0:
            x = -1*do
            p = -1*(di//x)
            return p
        elif di < 0 and do > 0:
            y = -1*di
            q = -1*(y//do)
            return q
        elif di == 0:
            return 0
        elif di < 0 and do < -1:
            di = -1*di
            do = -1*do
            l = (di//do)
            return l
        elif di == -1 and do == -1:
            return 1
        else:
            m , n = (di),(do)
            t = (m//n)-1
            return t