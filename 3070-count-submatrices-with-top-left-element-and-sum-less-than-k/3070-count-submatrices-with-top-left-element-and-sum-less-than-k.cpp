class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int rows = grid.size();
        int cols = grid[0].size();
        int count = 0;

        for(int r = 0; r < rows; ++r){
            for(int c = 0; c < cols; ++c){
                if(c > 0){
                    grid[r][c]+= grid[r][c-1];
                }
                if(r > 0){
                    grid[r][c]+= grid[r-1][c];
                }
                if(c > 0 && r > 0){
                    grid[r][c]-=grid[r-1][c-1];
                }

                if(grid[r][c] <= k){
                    count++;
                }
                else{
                    break;
                }
            }
        }

        return count;
        

    }
};