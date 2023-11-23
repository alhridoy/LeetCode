class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        
        for n1,n2 in edges:
            #undirected
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            #everysingle neighbours of i
            for j in adj[i]:
                if j == prev:
                    continue
                #call dfs on j swap value
                #check loop
                if not dfs(j, i):
                    return False
            return True
        return dfs(0,0) and n == len(visit)
        