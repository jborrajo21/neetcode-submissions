class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def backtrack(state, total, start):
            if total == target:
                combs.append(state.copy())
                return
            last = -1
            for i in range(start, len(candidates)):
                if candidates[i] == last: continue
                if total + candidates[i] > target: continue
                state.append(candidates[i])
                backtrack(state, total + candidates[i], i+1)
                last = state.pop()
            return
        
        backtrack([], 0, 0)
        return combs