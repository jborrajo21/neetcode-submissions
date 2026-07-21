class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def backtrack(state, start):
            subsets.append(state.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: continue
                state.append(nums[i])
                backtrack(state, i + 1)
                state.pop()
        
        backtrack([], 0)
        return subsets