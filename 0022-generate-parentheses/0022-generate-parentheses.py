class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        
        ans=[]
        self.backtrack(n,0,0,"",ans)
        return ans
    
    def backtrack(self,n,openb,closeb,curr_set,ans):
        if len(curr_set)==2*n:
            ans.append(curr_set)
            return 
        if openb<n:
            self.backtrack(n,openb+1,closeb,curr_set+"(",ans)
           
        if closeb<openb:
            self.backtrack(n,openb,closeb+1,curr_set+")",ans)