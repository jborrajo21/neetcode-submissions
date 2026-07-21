class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        def backtrack(state, total, start):
            if total == target:
                combs.append(state.copy())
                return
            if total > target: 
                return
            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(state, total + nums[i], i)
                state.pop()
            return

        backtrack([], 0, 0)
        return combs