class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        g = [i for i in range(len(points))] 
        sizes = [1 for _ in range(len(points))] 

        def root(v):
            i = v
            while i != g[i]:
                i = g[g[i]]
            return i
        
        def connected(u,v):
            return root(u) == root(v)
        
        def union(u,v):
            r1,r2 = root(u), root(v)
            if sizes[r1] > sizes[r2]:
                g[r2] = r1
                sizes[r1] += sizes[r2]
            else:
                g[r1] = r2
                sizes[r2] += sizes[r1]
        
        
        edges = []
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        
        heapq.heapify(edges)
        mst = 0
        for _ in range(len(points) - 1):
            while edges:
                cost, u, v = heapq.heappop(edges)
                if not connected(u,v):
                    mst += cost
                    union(u,v)
                    break

        return mst 
