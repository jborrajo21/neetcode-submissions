class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(set)
        for course, req in prerequisites:
            g[req].add(course)

        def dfs(r):
            path.add(r)
            for c in g[r]:
                if c in path or not dfs(c):
                    return False
            del g[r]
            path.remove(r)
            return True

        for req in [r for r in g]:
            path = set()
            if not dfs(req):
                return False
        return True