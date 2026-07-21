class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        nums.sort()
        def backtrack(state, total, start):
            if total == target:
                combs.append(state.copy())
                return
            for i in range(start, len(nums)):
                if total + nums[i] > target: 
                    return
                state.append(nums[i])
                backtrack(state, total + nums[i], i)
                state.pop()
            return

        backtrack([], 0, 0)
        return combs