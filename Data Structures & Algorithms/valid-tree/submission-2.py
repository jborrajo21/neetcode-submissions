class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(set)
        for p, c in edges:
            g[p].add(c)
            g[c].add(p)

        visited = set()

        def dfs(node, p):
            visited.add(node)
            for n in g[node]:
                if n == p:
                    continue
                if n in visited or not dfs(n, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n