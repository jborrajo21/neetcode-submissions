class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = [n for n in range(len(edges))]
        sizes = [0] * len(edges)

        def find(u,v):
            return root(u) == root(v)

        def union(u,v):
            r1 = root(u)
            r2 = root(v)
            if sizes[r1] > sizes[r2]:
                g[r2] = r1
                sizes[r1] += sizes[r2]
            else:
                g[r1] = r2
                sizes[r2] += sizes[r1]

        def root(n):
            node = n - 1
            while g[node] != node:
                g[node] = g[g[node]]
                node = g[node]
            return node
        
        idx = 0
        for i in range(len(edges)):
            u,v = edges[i]
            if find(u,v):
                idx = i
            union(u,v)
        
        return edges[idx]

