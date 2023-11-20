class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n= len(grid[0])
        
        
        
        def sinkIsland(row,col):
            
            grid[row][col]='0'
            
            #sink the neighbours too
            
            for r,c in [(row+1,col), (row-1,col),(row,col+1),(row,col-1)]:
                if 0 <=r<m and 0 <=c<n and grid[r][c]=='1':
                    sinkIsland(r,c)

        num_of_islands = 0
        
        for row in range(m):
            for col in range(n):
                
                if grid[row][col]=='1':
                    num_of_islands+=1
                    #sink the whole island
                    sinkIsland(row,col)
        return num_of_islands
        