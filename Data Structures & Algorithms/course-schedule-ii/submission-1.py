class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for course, req in prerequisites:
            g[req].add(course)

        state = [0] * numCourses
        stack = []
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            state[node] = 1
            for n in g[node]:
                if state[n] == 1:
                    has_cycle = True
                    return
                if state[n] == 0:
                    dfs(n)
            state[node] = 2
            stack.append(node)

        for n in range(numCourses):
            if state[n] == 0:
                dfs(n)
        
        return [] if has_cycle else stack[::-1]
