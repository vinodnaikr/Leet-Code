class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m=grid.size();
        int n=grid[0].size();
        vector<vector<int>> result(m-k+1,vector<int>(n-k+1));

        for(int x=0;x<=m-k;x++){
            for(int y=0;y<=n-k;y++){
                vector<int> elements;

                for(int i=x;i<x+k;i++){
                    for(int j=y;j<y+k;j++){
                        elements.push_back(grid[i][j]);
                    }
                }

                sort(elements.begin(),elements.end());

                int minDiff=INT_MAX;

                for(int i=1;i<elements.size();i++){
                    if(elements[i]!=elements[i-1]){
                        int diff=elements[i]-elements[i-1];
                        minDiff=min(minDiff,diff);
                        if(minDiff==1){
                            break;
                        }
                    }
                }

                result[x][y]=(minDiff==INT_MAX) ? 0 : minDiff;
            }
        }
        return result;
        
    }
};