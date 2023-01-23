class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d=collections.defaultdict(int)
        d2=collections.defaultdict(int)
        for i in trust:
            d[i[0]]+=1
            d2[i[1]]+=1
        l=[]    
        for i in range(1,N+1):    
            if(d[i]==0):
                l.append(i)
        ans='a'        
        for i in l:
            if(d2[i]==N-1):
                ans=i
                break
        if(ans=='a'):
            return -1
        return ans
            
               
            
            