class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])
        
        #check path we explored
        
        path = set()
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r  <0 or c <0 or
               r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                
                (r,c) in path
                ):
                return False
            #we found a character we need
            path.add((r,c))
            
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1)
                  ) # if any of the return true our results will retur True
            #remove the path we do not need
            path.remove((r,c))
            return res
        
        #brute force go thrw every single position in the grid and run dfs
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        #we did not find any words
        return False
                    
        
        