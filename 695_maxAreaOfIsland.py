# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:08:43 2019

@author: fed
"""

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) 
    {
        if(!grid.size()) return 0;
        int m = grid.size(),n = grid[0].size();
        int res = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    int s = 0;
                    dfs(grid,i,j,s);
                    res = max(res,s);
                }
            }
        }
        return res;
    }
    
    void dfs(vector<vector<int>> &grid, int i,int j, int &s)
    {
        if(i>=0 && i<grid.size() && j>=0 && j<grid[0].size())
        {
            if(grid[i][j]==1)
            {
                grid[i][j] = -1; //标记为访问过
                s++;
                dfs(grid,i-1,j,s);
                dfs(grid,i+1,j,s);
                dfs(grid,i,j-1,s);
                dfs(grid,i,j+1,s);
            }
        }
    }
};
            
            
            
            
            
            