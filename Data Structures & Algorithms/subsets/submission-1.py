class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        def backtrack(state, start):
            sets.append(state.copy())
            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(state, i + 1)
                state.pop()
            return

        backtrack([], 0)
        return sets