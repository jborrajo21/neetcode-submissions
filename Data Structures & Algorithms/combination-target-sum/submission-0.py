class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        def backtrack(state, start):
            if state[1] == target:
                combs.append(state[0].copy())
                return
            if state[1] > target: 
                return
            for i in range(start, len(nums)):
                state[0].append(nums[i])
                state[1] += nums[i] 
                backtrack(state, i)
                state[1] -= nums[i]
                state[0].pop()
            return

        backtrack([[], 0], 0)
        return combs