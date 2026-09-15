class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        dist = [float("inf")] * n
        dist[0] = 0
        mst = 0

        for _ in range(n):
            node = -1
            for v in range(n):
                if v not in visited and (node == -1 or dist[v]<dist[node]):
                    node = v
            visited.add(node)
            mst += dist[node]
            
            for v in range(n):
                if v not in visited:
                    dist[v] = min(dist[v],
                    abs(points[node][0] - points[v][0]) + 
                    abs(points[node][1] - points[v][1]))
        
        return mst