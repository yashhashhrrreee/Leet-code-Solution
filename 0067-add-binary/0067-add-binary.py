class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        a1, b1, res = ["0"] * 256, ["0"] * 256, ["0"] * 256
        for i, bit in enumerate(a[::-1]):
            a1[i] = bit
        for i, bit in enumerate(b[::-1]):
            b1[i] = bit

        a1.reverse()
        b1.reverse()
        # print(a1,b1) 
        carry = "0"
        for i in range(255, -1, -1):
            if a1[i] == "1" and b1[i] == "1":
                res[i] = "1" if carry == "1" else "0"
                carry = "1"
            elif (a1[i] == "0" and b1[i] == "1") or (a1[i] == "1" and b1[i] == "0"):
                if carry == "1":
                    res[i] = "0"
                else: 
                    res[i] = "1"
                    carry = "0"
            else:
                res[i] = "1" if carry == "1" else "0"
                carry = "0"
        
        res = "".join(res)
        return res.lstrip("0")