class Solution:
    def myAtoi(self, s: str) -> int:
        
        d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,"7":7,'8':8,'9':9,"0":0}
        
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        ans = ""
        neg = False
        pos = False
        isNum = False

        for i in s:
            if i in "-" and pos == False and isNum == False:
                neg = True
                isNum = True
            
            elif i in "+" and neg == False and isNum == False:
                pos = True
                isNum = True
            
            elif i in " " and isNum == False:
                continue
            
            elif i in "1234567890":
                ans =  i + ans
                isNum = True

            elif i not in "1234567890" and isNum == True:
                break
            else:
                break

            # print(ans)
        
        num = 0
        for i in range(len(ans)):
            num += d[ans[i]]*(10**i)
        if neg:
            num = -1*num

        if num >= (2**31 - 1) and not neg: 
            return MAX_INT
        if num <= (-2**31) and neg: 
            return MIN_INT
        else:
            return num