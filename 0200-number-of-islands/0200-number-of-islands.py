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
        '''
        Time Complexity 
�
(
�
�
)
O(nm). This might be surprising because there are 2 for loops, and then an additional recursion on sinkIsland. But notice that the total number of times sinkIsland gets called is always 
≤
�
(
�
�
)
≤O(nm) since once it visits a location, it never visits it again. This means we do 
�
(
�
�
)
O(nm) operations for the for loop, and 
�
(
�
�
)
O(nm) for sinkIsland, which is a total of 
�
(
�
�
)
O(nm).

Space Complexity 
�
(
1
)
O(1). Technically we're storing 
�
�
nm entries to mark each island as visited, but none of that is extra space. It's all being done using the space already given to us in the grid.
        '''