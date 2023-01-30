class Solution {
public:
     //Space Optimization
     int tribonacci(int n) {
        if(n==0) return 0;
        else if(n<=2) return 1;
        int a = 0,b = 1,c = 1;
        int ans = 0;
        for(int i = 3; i<=n;i++){
            ans = a+b+c;
            a=b;
            b=c;
            c=ans;
        }
        return ans;
     }
};