class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for n in g[node]:
                if n not in visited:
                    dfs(n)
        
        cc = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cc+=1
        
        return cc

