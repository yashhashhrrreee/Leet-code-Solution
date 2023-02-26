class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n,vector<int>(n,0));
        int x = 1,sr=0,sc=0,er=n-1,ec=n-1,i;
        while(sr<=er&&sc<=ec){
            for(i=sc;i<=ec;i++){
                ans[sr][i]  = x++;
            }sr++;
            for(i = sr; i<= er; i++){
                ans[i][ec] = x++;
            }
            ec--;
            for(i = ec; i>=sc; i--){
                ans[er][i] = x++;
            }
            er--;
            for(i = er; i>= sr; i--){
                ans[i][sc] = x++;
            }
            sc++;
        }
        return ans;
    }
};