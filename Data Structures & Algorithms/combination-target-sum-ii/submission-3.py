class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def bt(state, total, start):
            if total == target:
                combs.append(state.copy())
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                state.append(candidates[i])
                bt(state, total + candidates[i], i + 1)
                state.pop()
            return
        
        bt([], 0, 0)
        return combs